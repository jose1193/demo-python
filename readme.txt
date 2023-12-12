-- Build Image ----
docker build -t nombre-imagen -f Dockerfile.dockerfile .

---- Run and Assign Container Name With Image -------------
docker run --name mi_contenedor -p 5000:5000 nombre_de_la_imagen

-- Run ---
docker run -p 5000:5000 nombre-aplicacion


-- Stop Container---
docker ps
docker stop nombre_del_contenedor

--- Stop and Delete Container ----------
docker rm -f nombre_del_contenedor

---- Delete Image ---------------
 docker rmi nombre_imagen




