# AI Nav（导航站）

一个“AI 工具与资源导航站”示例项目，包含：
- 前端：Vue 3 + TypeScript + Vite + Vue Router + Tailwind CSS
- 后端：Flask + SQLAlchemy + Marshmallow（REST API）
- 部署：Docker + Nginx（前端静态站点 + /api 反向代理）

## 模块说明

### 前端（Web）
- 页面路由：[router/index.ts](file:///Users/m684621/Downloads/AAA/ITGang/AINav/src/router/index.ts)
  - `/` 首页：展示热门分类（已接入接口 `/api/categories`）
  - `/category/:slug` 分类页（Stub）
  - `/site/:id` 站点详情页（Stub）
  - `/search` 搜索页（Stub）
  - `/user/login` 登录页（Stub）
  - `/user/register` 注册页（Stub）
  - `/user/dashboard` 用户面板（Stub）
- 布局组件：
  - [Navbar.vue](file:///Users/m684621/Downloads/AAA/ITGang/AINav/src/components/Navbar.vue)：顶部导航（含主题切换入口）
  - [Footer.vue](file:///Users/m684621/Downloads/AAA/ITGang/AINav/src/components/Footer.vue)：页脚
- 主题能力：[useTheme.ts](file:///Users/m684621/Downloads/AAA/ITGang/AINav/src/composables/useTheme.ts)（light/dark，本地存储 + 系统偏好）

### 后端（API 服务）
- 应用工厂与蓝图注册：[api/__init__.py](file:///Users/m684621/Downloads/AAA/ITGang/AINav/api/__init__.py)
  - API 统一前缀：`/api`
- 路由定义：[api/routes.py](file:///Users/m684621/Downloads/AAA/ITGang/AINav/api/routes.py)
  - `GET /api/categories`：获取根分类列表（按 sort_order 排序，返回带 children）
  - `GET /api/sites`：获取站点列表（支持分页与筛选）
    - query：`page`（默认 1）、`per_page`（默认 20）、`category_id`、`keyword`
  - `GET /api/sites/{id}`：获取站点详情，并自增 visit_count
  - `POST /api/auth/register`：未实现（返回 501）
  - `POST /api/auth/login`：未实现（返回 501）
- 数据模型：[api/models.py](file:///Users/m684621/Downloads/AAA/ITGang/AINav/api/models.py)
  - User / Category / Site / Favorite / SiteSubmission / VisitLog
- 序列化与校验：[api/schemas.py](file:///Users/m684621/Downloads/AAA/ITGang/AINav/api/schemas.py)
- 数据库迁移：`migrations/`（Flask-Migrate/Alembic）
- 初始化数据脚本：[api/seed.py](file:///Users/m684621/Downloads/AAA/ITGang/AINav/api/seed.py)（示例分类、站点、测试用户）

### 部署与基础设施
- Docker 编排：[docker-compose.yml](file:///Users/m684621/Downloads/AAA/ITGang/AINav/docker-compose.yml)
  - `frontend`：对外端口 `80`
  - `backend`：对外端口 `5000`
  - `db`（MySQL）：对外端口 `3306`
  - `redis`：对外端口 `6379`
  - `adminer`：对外端口 `8080`
- Nginx 反向代理：[nginx.conf](file:///Users/m684621/Downloads/AAA/ITGang/AINav/nginx.conf)
  - `location /`：SPA 路由回退到 `index.html`
  - `location /api`：转发到 `backend:5000`

## 访问地址（URL）

### 本地开发（推荐）
- 前端：`http://localhost:5173/`
  - 通过 Vite Proxy 将 `/api` 转发到后端（见 [vite.config.ts](file:///Users/m684621/Downloads/AAA/ITGang/AINav/vite.config.ts#L13-L22)）
- 后端：`http://127.0.0.1:5000/`
  - API 基础地址：`http://127.0.0.1:5000/api`
  - 示例：`GET http://127.0.0.1:5000/api/categories`

### Docker（生产形态）
- 前端（Nginx）：`http://localhost/`（80）
- API（同域代理）：`http://localhost/api`
  - 示例：`GET http://localhost/api/categories`
- Adminer：`http://localhost:8080/`（数据库管理界面）

## 当前实现状态
- 前端仅首页完成接口联调；其余页面为占位 Stub。
- 后端 auth 登录/注册接口为占位（返回 501），其余分类/站点相关接口可用。
