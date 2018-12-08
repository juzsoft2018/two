# -*- coding: utf-8 -*-

from odoo import api, fields, models

class TrainingSubject(models.Model):
    _name = 'pscloud.training.subject'
    _description = "客户"

    name = fields.Char(string='姓名')
    lxfs = fields.Char( string='联系方式')
    dz   = fields.Char(string='地址')
    desc = fields.Text(string='描述')

#  vim:et:si:sta:ts=4:sts=4:sw=4:tw=79:
