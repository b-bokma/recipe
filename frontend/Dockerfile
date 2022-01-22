FROM node:lts-alpine AS build-stage

# install simple http server for serving static content
RUN npm install -g npm@latest

WORKDIR /vue-app

# Copy the package.json and install dependencies
COPY package*.json ./
RUN npm install --loglevel=error

# copy files and folders to the current working directory (i.e. 'vue-app' folder)
COPY . .

# build app for production with minification
RUN npm run build


FROM nginx:alpine as production-build
#COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
## Remove default nginx index page
#RUN rm -rf /usr/share/nginx/html/*

# Copy from the stahg 1
COPY --from=build-stage /vue-app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]




