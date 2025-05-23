# プロジェクトの目的
複数のユーザーが使用できるToDoアプリを構築することを目的としています。
DjangoとDjango REST Frameworkを使用し、WebアプリとAPIの両方を実装しています。

## 機能
1. 投稿のCRUD機能: タスクの作成(Create)、閲覧(Read)、編集(Update)、削除(Delete)を実装。
2. ユーザー認証: サインアップ、ログイン、ログアウト機能を追加。
3. 検索、並び替え機能: タスクの部分検索、作成日、締め切りによる並べ替え。
4. 期限超過タスクの強調表示機能: 期限超過タスクの文字を赤色、強調表示する。
5. 完了タスクの一括削除： 完了状態のタスクを一括削除する
6. API機能: タスク一覧、詳細の取得、追加、編集、削除機能
   
## 使用技術
**バックエンド**
1. Django 5.2.1
2. Django REST Framework 3.16.0
3. djoser 2.3.1

**データベース**
1. SQLite(デフォルト)

## APIエンドポイント
|  メソッド   |  エンドポイント  |  説明  | 
| --- | --- | --- | 
| POST | /api/auth/users/  |  ユーザー登録   | 
| POST | /api/auth/token/login/  |  ログイン（トークン取得）   | 
| POST | /api/auth/token/logout/  |  ログアウト   | 
| GET | /api/tasks/  |  タスク一覧取得   | 
| POST | /api/tasks/  |  タスク作成   | 
| GET | /api/tasks/{id}/  |   タスク詳細の取得  |
| PATCH | /api/tasks/{id}/  |   タスク編集  | 
| DELETE | /api/tasks/{id}/  |   タスク削除  | 
