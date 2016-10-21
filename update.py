# coding:utf-8
import re

from openerp import api, fields, models
from openerp import exceptions


class UpdateWay(models.Model):
    _name = 'api.update.way'
    name = fields.Text(
        string=''
    )
    _defaults = {'name': '更新'}

    remarks = fields.Text(
        string="备注",
    )
    update_special = fields.One2many(
        comodel_name="api.update.ios",
        inverse_name='api_special_update_id',
        string='iOS更新',
    )
    update_general = fields.One2many(
        comodel_name="api.update.android",
        inverse_name="api_general_update_id",
        string="Android更新",
    )


class UpdateSpecialInformation(models.Model):  # iOS更新
    _name = 'api.update.ios'
    _order = 'version desc'

    api_special_update_id = fields.Many2one(
        comodel_name="api.update.way",
        string='Special Update',
        ondelete='cascade',
    )
    update_url = fields.Char(
        string="url",
        required=True
    )
    update_title = fields.Char(
        string="提示标题",
    )
    update_interval = fields.Integer(
        "时间间隔",
    )
    update_limittimes = fields.Integer(
        "提示次数",
    )
    phone_model = fields.Char(
        string="手机型号",
    )
    channel_number = fields.Char(
        string="渠道号",
    )
    update_date = fields.Datetime(
        string="更新日期",
    )
    update_size = fields.Char(
        string="大小",
        required=True
    )
    version = fields.Char(
        string="版本号",
        required=True
    )
    update_note = fields.Text(
        string="更新日志",
    )
    system_type = fields.Char(
        string="系统类型",
        default='iOS',

    )
    power_update = fields.Selection(
        string="是否强制更新",
        selection=[('0', '非强制更新'), ('1', '强制更新')],
        default='0',

    )

    @api.constrains('version', 'update_url')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.version:
                version = r.version
                regex = re.compile(
                    r'^[0-9]+\.[0-9]+\.[0-9]{1,}$', re.IGNORECASE
                )
                m = regex.match(version)
                if not m:
                    raise exceptions.ValidationError("正确的版本格式应如:0.0.1")
            if r.update_url:
                regex = re.compile(
                    r'^(?:http|ftp)s?://'
                    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
                    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                    r'(?::\d+)?'
                    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
                m = regex.match(r.update_url)
                if not m:
                    raise exceptions.ValidationError(
                        "正确的url格式应如:http://fir.im/x3t6")


class UpdateGeneralInformation(models.Model):  # Android更新
    _name = 'api.update.android'
    _order = 'version desc'

    channel_number = fields.Char(
        string="渠道号",
    )
    update_url = fields.Char(
        string="url",
        required=True
    )
    update_title = fields.Char(
        string="提示标题",
    )
    update_interval = fields.Integer(
        "时间间隔",
    )
    update_limittimes = fields.Integer(
        "提示次数",
    )
    phone_model = fields.Char(
        string="手机型号",
    )
    api_general_update_id = fields.Many2one(
        comodel_name="api.update.way",
        string='General Update',
        ondelete='cascade',
    )
    update_date = fields.Datetime(
        string="更新日期",
    )
    update_size = fields.Char(
        string="大小",
        required=True
    )
    version = fields.Char(
        string="版本号",
        required=True
    )
    update_note = fields.Text(
        string="更新日志",
    )
    system_type = fields.Char(
        string="系统类型",
        default='Android',

    )
    power_update = fields.Selection(
        string="是否强制更新",
        selection=[('0', '非强制更新'), ('1', '强制更新')],
        default='0',

    )

    @api.constrains('version', 'update_url')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.version:
                version = r.version
                regex = re.compile(
                    r'^[0-9]+\.[0-9]+\.[0-9]{1,}$', re.IGNORECASE
                )
                m = regex.match(version)
                if not m:
                    raise exceptions.ValidationError("正确的版本格式应如:0.0.1")
            if r.update_url:
                regex = re.compile(
                    r'^(?:http|ftp)s?://'
                    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
                    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                    r'(?::\d+)?'
                    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
                m = regex.match(r.update_url)
                if not m:
                    raise exceptions.ValidationError(
                        "正确的url格式应如:http://fir.im/x3t6")
