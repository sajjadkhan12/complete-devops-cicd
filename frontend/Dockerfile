# Build stage
FROM node:20-alpine AS builder

# Set working directory
WORKDIR /app

# Accept build arguments for environment variables
ARG VITE_POEM_API_URL=/api/poem
ARG VITE_QUOTE_API_URL=/api/quote

# Set environment variables for Vite build
ENV VITE_POEM_API_URL=$VITE_POEM_API_URL
ENV VITE_QUOTE_API_URL=$VITE_QUOTE_API_URL

# Copy package files
COPY package.json package-lock.json* ./

# Install all dependencies (including devDependencies for build)
# Using npm install instead of npm ci to handle lockfile mismatches
RUN npm install --legacy-peer-deps && npm cache clean --force

# Copy source code
COPY . .

# Build the application
RUN npm run build

# Production stage - simple static file server
FROM nginx:alpine

# Simple nginx config to serve static files
RUN echo 'server { \
    listen 80; \
    server_name localhost; \
    root /usr/share/nginx/html; \
    index index.html; \
    location / { \
        try_files $uri $uri/ /index.html; \
    } \
    location /health { \
        access_log off; \
        return 200 "healthy\n"; \
        add_header Content-Type text/plain; \
    } \
}' > /etc/nginx/conf.d/default.conf

# Copy built files from builder
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose port
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --quiet --tries=1 --spider http://localhost/health || exit 1

# Start nginx
CMD ["nginx", "-g", "daemon off;"]

