#!/bin/bash

# Script to update GKE node pool machine type to e2-medium
# Usage: ./scripts/update-node-pool.sh

# Get values from environment or use defaults
PROJECT_ID=${GCP_PROJECT_ID:-"your-project-id"}
CLUSTER_NAME=${GKE_CLUSTER_NAME:-"my-cluster"}
ZONE=${GKE_ZONE:-"us-central1-a"}
NODE_POOL_NAME=${NODE_POOL_NAME:-"default-pool"}  # Change this if your node pool has a different name

echo "Updating node pool machine type to e2-medium..."
echo "Project: $PROJECT_ID"
echo "Cluster: $CLUSTER_NAME"
echo "Zone: $ZONE"
echo "Node Pool: $NODE_POOL_NAME"

# Update the node pool machine type
gcloud container node-pools update $NODE_POOL_NAME \
  --cluster=$CLUSTER_NAME \
  --zone=$ZONE \
  --machine-type=e2-medium \
  --project=$PROJECT_ID

echo "Node pool update initiated. This will cause nodes to be recreated."
echo "Note: Existing nodes will be drained and recreated with the new machine type."

