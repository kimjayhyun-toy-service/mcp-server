from contextlib import asynccontextmanager

import uvicorn
from dependency_injector.wiring import Provide, inject
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

import _version
from container import Container
from domain.organization.route import router as organization_router
from utils import load_config

# from py_eureka_client import eureka_client


@asynccontextmanager
@inject
async def lifespan(
    app: FastAPI,
    logger=Depends(Provide[Container.logger]),
):
    # 서비스 시작 시
    yield  # 애플리케이션이 실행되는 동안 여기서 대기

    # 서비스 종료 시


# FastAPI 앱 설정
app = FastAPI(
    title=_version.__appdesc__,
    description="",
    version="1.0.0",
    openapi_url="/v2/api-docs",
    docs_url="/v2/docs",
    redoc_url="/v2/redoc",
    lifespan=lifespan,
)


# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router 설정
app.include_router(organization_router, tags=["Organization"])


def main():
    import domain.organization.route

    container = Container()

    config = load_config(app_description=_version.__appdesc__)

    container.config.from_dict(config)

    container.wire(modules=[__name__, domain.organization.route])

    # FastAPI 앱 실행
    uvicorn.run(app, host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
