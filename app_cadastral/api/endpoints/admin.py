# from fastapi import APIRouter, HTTPException

# from app_cadastral.core.user import auth_backend, fastapi_users
# from app_cadastral.schemas.user import UserCreate, UserRead, UserUpdate

# # router = APIRouter()

# from fastapi import FastAPI

# # from fastadmin import fastapi_app as admin_app

# # app = FastAPI()

# # app.mount("/admin", admin_app)




# # router.include_router(
# #     fastapi_users.get_auth_router(auth_backend),
# #     prefix='/auth/jwt',
# #     tags=['auth'],
# # )
# # router.include_router(
# #     fastapi_users.get_register_router(UserRead, UserCreate),
# #     prefix='/auth',
# #     tags=['auth'],
# # )
# # router.include_router(
# #     fastapi_users.get_users_router(UserRead, UserUpdate),
# #     prefix='/users',
# #     tags=['users'],
# # )


# # @router.delete(
# #     '/users/{id}',
# #     tags=['users'],
# #     deprecated=True
# # )
# # def delete_user(id: str):
# #     """Не используйте удаление, деактивируйте пользователя."""
# #     raise HTTPException(
# #         status_code=405,
# #         detail='Удаление пользователей запрещено!'
# #     )
