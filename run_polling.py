import os

import uvicorn

if __name__ == "__main__":
    os.environ["TGBOT_IS_POLLING"] = "1"
    uvicorn.run(
        "app.api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
