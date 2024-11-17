# Telegram Bot template

Telegram Bot template

## Deployment

The project uses GitHub Actions with Ansible for automated deployments. We have two deployment workflows:

### Production Deployment (Blue-Green)

The production deployment uses a blue-green deployment strategy to ensure zero downtime. When code is pushed to the `main` branch, it:

1. Builds a Docker image
2. Deploys using blue-green strategy (alternating between two containers)
3. Performs health checks before switching traffic
4. Uses Nginx as a reverse proxy

Required GitHub Secrets:
- `DEPLOY_SSH_KEY`: SSH private key for production server
- `DEPLOY_HOST`: Production server hostname/IP
- `DEPLOY_USER`: SSH user for deployment

### Development Deployment (Fast Deploy)

For the development environment, we use a simpler, faster deployment process. When code is pushed to the `develop` branch, it:

1. Stops any existing development container
2. Builds and deploys a new container in one step
3. Performs quick health checks

Required GitHub Secrets:
- `DEV_DEPLOY_SSH_KEY`: SSH private key for development server
- `DEV_DEPLOY_HOST`: Development server hostname/IP
- `DEV_DEPLOY_USER`: SSH user for development deployment

### Port Configuration

- Production:
  - Nginx: Port 80
  - Blue Container: Port 48001
  - Green Container: Port 48002

- Development:
  - Direct container access: Port 48000

### Health Checks

Both environments use the `/health` endpoint to verify successful deployment. The endpoint returns:

```

"""
Project documentation covering:
- Deployment workflows for both production and development
- Configuration requirements and environment setup
- Port mappings and infrastructure details
- Health check implementation and monitoring
"""