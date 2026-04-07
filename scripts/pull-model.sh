#!/bin/bash
# Pull Gemma 4 E4B model for Ollama
# Usage: ./scripts/pull-model.sh

set -e

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "========================================"
echo "  Pulling Gemma 4 E4B Model"
echo "========================================"
echo ""

# Check if Ollama container is running
if ! docker ps | grep -q ollama; then
    echo -e "${RED}ERROR: Ollama container is not running${NC}"
    echo "Please start services first:"
    echo "  cd docker && docker-compose up -d"
    exit 1
fi

# Wait for Ollama to be ready
echo "Waiting for Ollama to be ready..."
MAX_WAIT=30
WAITED=0
WAIT_INTERVAL=2

while [ $WAITED -lt $MAX_WAIT ]; do
    if docker exec ollama ollama list &>/dev/null; then
        echo -e "${GREEN}✓ Ollama is ready${NC}"
        break
    fi
    echo "  Waiting... ($WAITED seconds)"
    sleep $WAIT_INTERVAL
    WAITED=$((WAITED + WAIT_INTERVAL))
done

if [ $WAITED -ge $MAX_WAIT ]; then
    echo -e "${RED}ERROR: Ollama is not responding${NC}"
    exit 1
fi

# Check if model already exists
echo ""
echo "Checking if model exists..."
if docker exec ollama ollama list 2>/dev/null | grep -q "gemma4:e4b"; then
    echo -e "${GREEN}✓ Model already downloaded${NC}"
    docker exec ollama ollama list
    exit 0
fi

# Pull model
echo ""
echo -e "${YELLOW}Downloading Gemma 4 E4B model...${NC}"
echo "This may take several minutes depending on your connection."
echo ""

if docker exec ollama ollama pull gemma4:e4b; then
    echo ""
    echo -e "${GREEN}========================================"
    echo "  Model downloaded successfully!"
    echo "========================================${NC}"
    echo ""
    echo "Verify:"
    docker exec ollama ollama list
else
    echo ""
    echo -e "${RED}ERROR: Failed to download model${NC}"
    exit 1
fi
