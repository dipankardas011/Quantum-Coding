# the resources
https://qiskit.org/textbook/ch-states/introduction.html

```bash
docker build -t quantum-img:local .
docker run --rm -it -v ${PWD}:/app -p 8888:8888 quantum-img:local
```
