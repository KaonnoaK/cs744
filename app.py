from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    counter = str(redis.get('hits'),'utf-8')
    return "This webpage has been viewed "+counter+" time(s)"
@app.route("/compute")
def compute():
    # Simple CPU-bound computation (recursive Fibonacci)
    def fib(n):
        return n if n < 2 else fib(n-1) + fib(n-2)
    result = fib(36)
    return f"Fibonacci(36) = {result}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
