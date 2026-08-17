# Bài 3 - Secure Learning Resource API

## API

| Method | Endpoint | Quyền |
|---|---|---|
| POST | `/auth/login` | Công khai |
| GET | `/users/me` | Đăng nhập |
| GET | `/resources` | User/Admin |
| GET | `/resources/{resource_id}` | User/Admin |
| POST | `/resources` | Admin |
| PATCH | `/resources/{resource_id}/publish` | Admin |
| DELETE | `/resources/{resource_id}` | Admin |
| GET | `/health` | Công khai |

## Tài khoản

- admin01 / 123456
- student01 / 123456
- student02 / 123456, tài khoản bị khóa

## Luồng

Frontend gửi request qua CORS Middleware. Custom Middleware tạo request ID, đo thời gian và ghi log. Router nhận request. Dependency xác thực JWT bằng chữ ký, exp và sub, sau đó tìm lại user trong hệ thống. Dependency phân quyền kiểm tra role. Service xử lý nghiệp vụ tài nguyên.

## HTTP status

- 400: dữ liệu request không hợp lệ theo nghiệp vụ.
- 401: token thiếu, sai chữ ký, hết hạn hoặc không xác định được tài khoản.
- 403: tài khoản bị khóa hoặc không đủ quyền.
- 404: tài nguyên không tồn tại hoặc user cố truy cập tài nguyên chưa xuất bản.

## Chạy

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
pytest
```

Swagger: `/docs`
