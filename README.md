# virt-lab2


curl -k https://$ROUTE/health/ready

Client / Load Balancer
        |
        | HTTPS /health/ready
        v
OpenShift Ingress Controller
        |
        v
Route health-demo
        |
        v
Service health-demo
        |
        v
Ready Pod
        |
        v
HTTP 200


curl -k -X POST https://$ROUTE/health/disable
curl -k https://$ROUTE/health/ready

health-demo-xxxxx   1/1 Running
        |
 POST /health/disable
        |
        v
/health/ready -> 503
        |
        v
readinessProbe falha
        |
        v
health-demo-xxxxx   0/1 Running
        |
        v
Endpoint retirado do Service


**Para reativá-lo, faça diretamente dentro do Pod:**

POD=$(oc get pod -l app=health-demo -o jsonpath='{.items[0].metadata.name}')

oc exec $POD -- \
  curl -X POST http://localhost:3333/health/enable

Ou, se curl não estiver instalado na imagem Python:

oc exec $POD -- python -c \
'import urllib.request; urllib.request.urlopen(urllib.request.Request("http://localhost:3333/health/enable", method="POST"))'







