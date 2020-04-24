FROM node as react-build
WORKDIR /app/client
COPY . ./
COPY package.json /app/client
RUN npm install
RUN npm run build

#  Stage 2 - the production environment
FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=react-build /app/client/build /usr/share/nginx/html
EXPOSE 80
EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]