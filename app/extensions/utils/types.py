#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "hoovada.com team"
__maintainer__ = "hoovada.com team"
__email__ = "admin@hoovada.com"
__copyright__ = "Copyright (c) 2020 - 2020 hoovada.com . All Rights Reserved."


class BaseType(object):
    pass


class UserRole(BaseType):
    SUPER_ADMIN = 'SUPER_ADMIN'
    ADMIN = 'ADMIN'

    @staticmethod
    def admin_all():
        return 'ADMIN', 'SUPER_ADMIN'

    @classmethod
    def is_admin(cls, role):
        all_admin = cls.admin_all()
        for r in (role or "").split(','):
            if r.strip() in all_admin:
                return True
        return False

    @classmethod
    def is_permission(cls, role_default, role):
        for r in (role or "").split(','):
            if r.strip() in role_default:
                return True
        return False

    @classmethod
    def is_super_admin(cls, role):
        for r in role.split(','):
            if r.strip() in [UserRole.SUPER_ADMIN]:
                return True
        return False


class PermissionType(BaseType):
    VOTE = 'VOTE'
    SHARE = 'SHARE'
    LIKE = 'LIKE'
    COMMENT = 'COMMENT'
    ANSWER = 'ANSWER'
    ANSWER_MEDIA = 'ANSWER_MEDIA'
    REPORT = 'REPORT'
    FAVORITE = 'FAVORITE'

    # Admin
    QUESTION_PERMISSION = 'QUESTION_PERMISSION'
    ARTICLE_PERMISSION = 'ARTICLE_PERMISSION'
    TOPIC_PERMISSION = 'TOPIC_PERMISSION'
    REPORT_PERMISSION = 'REPORT_PERMISSION'
    REQUEST_PERMISSION = 'REQUEST_PERMISSION'

    # Question
    QUESTION_VOTE = 'QUESTION_VOTE'
    QUESTION_SHARE = 'QUESTION_SHARE'
    QUESTION_LIKE = 'QUESTION_LIKE'
    QUESTION_COMMENT = 'QUESTION_COMMENT'
    QUESTION_SAVE = 'QUESTION_SAVE'
    QUESTION_REPORT = 'QUESTION_REPORT'
    QUESTION_FAVORITE = 'QUESTION_FAVORITE'

    # Answer
    ANSWER_VOTE = 'ANSWER_VOTE'
    ANSWER_SHARE = 'ANSWER_SHARE'
    ANSWER_LIKE = 'ANSWER_LIKE'
    ANSWER_COMMENT = 'ANSWER_COMMENT'
    ANSWER_SAVE = 'ANSWER_SAVE'
    ANSWER_REPORT = 'ANSWER_REPORT'
    ANSWER_FAVORITE = 'ANSWER_FAVORITE'

    @staticmethod
    def permission_all():
        return {'VOTE', 'SHARE', 'LIKE', 'COMMENT', 'ANSWER', 'ANSWER_MEDIA', 'REPORT', 'FAVORITE',
                # admin
                'ARTICLE_PERMISSION', 'QUESTION_PERMISSION', 'TOPIC_PERMISSION', 'REPORT_PERMISSION', 'REQUEST_PERMISSION',
                # answer
                'ANSWER_VOTE', 'ANSWER_SHARE', 'ANSWER_LIKE', 'ANSWER_COMMENT', 'ANSWER_SAVE', 'ANSWER_REPORT',
                'ANSWER_FAVORITE',
                # question
                'QUESTION_VOTE', 'QUESTION_SHARE', 'QUESTION_LIKE', 'QUESTION_COMMENT', 'QUESTION_SAVE',
                'QUESTION_REPORT', 'QUESTION_FAVORITE',
                # comment
                }
