from fastapi import APIRouter
from app.api.v1.endpoints import (
    analyses,
    comparisons,
    datasets,
    eda,
    health,
    jobs,
    quality,
)

api_router = APIRouter()

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(datasets.router, prefix="/datasets", tags=["Datasets"])
api_router.include_router(analyses.router, prefix="/analyses", tags=["Analyses"])
api_router.include_router(quality.router, prefix="/quality-assessments", tags=["Quality"])
api_router.include_router(eda.router, prefix="/eda-reports", tags=["EDA"])
api_router.include_router(comparisons.router, prefix="/comparisons", tags=["Comparisons"])
api_router.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
