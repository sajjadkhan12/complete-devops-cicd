FROM nginx:alpine

# Install gettext for envsubst
RUN apk add --no-cache gettext

# Copy nginx configuration template
COPY nginx.conf.template /etc/nginx/templates/default.conf.template

# Expose port
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --quiet --tries=1 --spider http://localhost/health || exit 1

# Start nginx with environment variable substitution
CMD ["/bin/sh", "-c", "envsubst '$$FRONTEND_SERVICE $$POEM_SERVICE $$QUOTE_SERVICE $$POEM_PORT $$QUOTE_PORT' < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]

