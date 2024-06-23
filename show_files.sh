#!/bin/bash

echo "=== Contents of api/ directory ==="
for file in api/*.py; do
    echo "=== $file ==="
    cat "$file"
    echo ""
done

echo "=== Contents of models/ directory ==="
for file in models/*.py; do
    echo "=== $file ==="
    cat "$file"
    echo ""
done

echo "=== Contents of persistence/ directory ==="
for file in persistence/*.py; do
    echo "=== $file ==="
    cat "$file"
    echo ""
done
