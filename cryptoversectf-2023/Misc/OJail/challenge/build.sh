docker stop ocamljail
docker rm ocamljail
docker build -t "ocaml" . 
docker run --name ocamljail -d -p 4201:4201 ocaml 
