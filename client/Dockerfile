FROM node as vue-build
WORKDIR /app/client
COPY . ./
COPY package.json /app/client
RUN npm install
RUN npm run build

#  Stage 2 - the production environment
FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=vue-build /app/client/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]