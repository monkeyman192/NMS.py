#!/bin/bash

# This script is copied directly from https://github.com/MathieuMoalic/action-python-package-new-version/blob/main/entrypoint.sh
# This is just until there is extra functionality as part of that repo to allow specifying a different index.

# Check if pyproject.toml exists
PYPROJECT_FILE=pyproject.toml

if [ ! -f "$PYPROJECT_FILE" ]; then
    error_exit "$PYPROJECT_FILE does not exist."
fi

# Step 1: Get version from pyproject.toml
VERSION=$(awk -F'=' '/^version/ {gsub(/[" ]/, "", $2); print $2}' "$PYPROJECT_FILE")
if [ -z "$VERSION" ]; then
    error_exit "Unable to extract version from $PYPROJECT_FILE"
fi
echo "Version is $VERSION"

INDEX="${PYPI_INDEX:-pypi.org}"

# Step 2: Get package name from pyproject.toml
PACKAGE_NAME=$(awk -F'=' '/^name/ {gsub(/[" ]/, "", $2); print $2}' "$PYPROJECT_FILE")
if [ -z "$PACKAGE_NAME" ]; then
    error_exit "Unable to extract package name from $PYPROJECT_FILE"
fi
echo "PACKAGE_NAME is $PACKAGE_NAME"

# Step 3: Get latest release version from PyPI
PUBLISHED_VERSIONS=$(curl -s "https://$INDEX/pypi/$PACKAGE_NAME/json" | jq -r '.releases | keys | .[]')

if [ -z "$PUBLISHED_VERSIONS" ]; then
    error_exit "Unable to retrieve published version from PyPI for $PACKAGE_NAME"
fi
echo "Published PyPI versions are $PUBLISHED_VERSIONS"

# Step 4: Check if current version is in the list of published versions
PUBLISHING="true"
for ver in $PUBLISHED_VERSIONS; do
    if [ "$ver" == "$VERSION" ]; then
        PUBLISHING="false"
        break
    fi
done

echo "PUBLISHING is $PUBLISHING"
echo "PUBLISHING=$PUBLISHING" >> $GITHUB_ENV
echo "PUBLISHING_${INDEX/./_}=$PUBLISHING" >> $GITHUB_ENV
echo "PACKAGE_VERSION=$VERSION" >> $GITHUB_ENV
