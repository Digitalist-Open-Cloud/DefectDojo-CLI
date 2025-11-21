#!/bin/bash
set -e

# Update version in pyproject.toml
# get version from pyproject.toml
version=$(grep -E '^version = ' pyproject.toml | cut -d '"' -f 2)


# Install/Update python3 build module
poetry install

# Build
poetry build

# Add pblush token (only needed once)
#poetry config pypi-token.pypi <your-token>

poetry publish

# Commit ChangeLog and tag
git tag -a "$version" -m "Release $version"

# Push to remote repo
git push origin main --follow-tags

sleep 60
docker build --build-arg VERSION=${version} . -t digitalist/defectdojo-cli2:$version --platform=linux/amd64 --no-cache
docker tag digitalist/defectdojo-cli2:$version digitalist/defectdojo-cli2:latest
docker push digitalist/defectdojo-cli2:$version
docker push digitalist/defectdojo-cli2:latest