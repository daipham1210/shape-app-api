# shape-app-api

- User APIs:
  + Register: http://127.0.0.1:8000/api/user/register/
  + Login (create JWT token): http://127.0.0.1:8000/api/user/login/
  
- Shape APIs:
  + Triangles: http://127.0.0.1:8000/api/shape/triangles/
  + Rectangles: http://127.0.0.1:8000/api/shape/rectangles/
  + Square: square also is rectangle so we reuse Rectangles Apis, add params is_square to get list squares
  + Diamonds: http://127.0.0.1:8000/api/shape/diamonds/
