# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.av_user import AVUser
from openapi_server.models.post import Post
from openapi_server import util

from openapi_server.models.av_user import AVUser  # noqa: E501
from openapi_server.models.post import Post  # noqa: E501

class Comment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, post=None, author=None, parent_comment=None, content=None):  # noqa: E501
        """Comment - a model defined in OpenAPI

        :param post: The post of this Comment.  # noqa: E501
        :type post: Post
        :param author: The author of this Comment.  # noqa: E501
        :type author: AVUser
        :param parent_comment: The parent_comment of this Comment.  # noqa: E501
        :type parent_comment: Comment
        :param content: The content of this Comment.  # noqa: E501
        :type content: str
        """
        self.openapi_types = {
            'post': Post,
            'author': AVUser,
            'parent_comment': Comment,
            'content': str
        }

        self.attribute_map = {
            'post': 'post',
            'author': 'author',
            'parent_comment': 'parentComment',
            'content': 'content'
        }

        self._post = post
        self._author = author
        self._parent_comment = parent_comment
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'Comment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Comment of this Comment.  # noqa: E501
        :rtype: Comment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def post(self):
        """Gets the post of this Comment.

        The post comment is replied to.  # noqa: E501

        :return: The post of this Comment.
        :rtype: Post
        """
        return self._post

    @post.setter
    def post(self, post):
        """Sets the post of this Comment.

        The post comment is replied to.  # noqa: E501

        :param post: The post of this Comment.
        :type post: Post
        """
        if post is None:
            raise ValueError("Invalid value for `post`, must not be `None`")  # noqa: E501

        self._post = post

    @property
    def author(self):
        """Gets the author of this Comment.

        Author of the comment.  # noqa: E501

        :return: The author of this Comment.
        :rtype: AVUser
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Comment.

        Author of the comment.  # noqa: E501

        :param author: The author of this Comment.
        :type author: AVUser
        """
        if author is None:
            raise ValueError("Invalid value for `author`, must not be `None`")  # noqa: E501

        self._author = author

    @property
    def parent_comment(self):
        """Gets the parent_comment of this Comment.

        Parent comment if this comment is replied to comment, otherwise set to `null`  # noqa: E501

        :return: The parent_comment of this Comment.
        :rtype: Comment
        """
        return self._parent_comment

    @parent_comment.setter
    def parent_comment(self, parent_comment):
        """Sets the parent_comment of this Comment.

        Parent comment if this comment is replied to comment, otherwise set to `null`  # noqa: E501

        :param parent_comment: The parent_comment of this Comment.
        :type parent_comment: Comment
        """

        self._parent_comment = parent_comment

    @property
    def content(self):
        """Gets the content of this Comment.

        Content of the comment.  # noqa: E501

        :return: The content of this Comment.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Comment.

        Content of the comment.  # noqa: E501

        :param content: The content of this Comment.
        :type content: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501
        if content is not None and len(content) < 1:
            raise ValueError("Invalid value for `content`, length must be greater than or equal to `1`")  # noqa: E501

        self._content = content
