from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    name = fields.Str(required=True, validate=validate.Length(min=2))
    avatar_url = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    slug = fields.Str(required=True)
    icon = fields.Str()
    parent_id = fields.Int(allow_none=True)
    sort_order = fields.Int()
    children = fields.Nested('CategorySchema', many=True, exclude=('children',), dump_only=True)

class SiteSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    url = fields.Str(required=True)
    description = fields.Str()
    icon_url = fields.Str()
    category_id = fields.Int(required=True)
    category = fields.Nested(CategorySchema, only=('id', 'name'), dump_only=True)
    visit_count = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

class SiteSubmissionSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    url = fields.Str(required=True)
    description = fields.Str()
    category_id = fields.Int(required=True)
    status = fields.Str(dump_only=True)
    reject_reason = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
