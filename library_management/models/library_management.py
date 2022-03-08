from email.policy import default
from odoo import models , fields
from odoo.exceptions import UserError,ValidationError
from dateutil.relativedelta import relativedelta


class LibraryManagement(models.Model) :
    _name = "library.books"
    _description = "Library data"

    name = fields.Char()
    description = fields.Text()
    image = fields.Image()
    category_id = fields.Many2one('books.category')
    isbn = fields.Integer()
    publisher = fields.Char()
    Copyright = fields.Char()
    edition = fields.Char()
    title = fields.Char()
    author = fields.Char()
    price = fields.Float()
    pages = fields.Integer()

    status = fields.Selection([
        ('available' , 'Available'),
        ('notavailable' , 'Not Available')], default = 'available')

    state = fields.Selection([
        ('issue' , 'Issue'),
        ('cancle' , 'Cancle')])


    def action_issue(self) :
        for record in self :
            record.state = 'issue'



class BookCategory(models.Model) :
    _name = "books.category"
    _description = "Book Category"

    name = fields.Char()


class BookRequest(models.Model) :
    _name = "book.request"
    _description = "Book Request"

    name = fields.Char()
    image = fields.Image()
    author = fields.Char()
    edition = fields.Char()
    publisher = fields.Char()
    request_by = fields.Many2one('res.users')
    request_date = fields.Date(default = lambda self: fields.Datetime.now(),copy=False)

class Book(models.Model):
    _name = "lib.book"
    _description = "Book"

    name = fields.Char()


class BookRegister(models.Model):
    _name = "book.register"
    _description ="Book Register"
    _rec_name = "book_id"
    # name = fields.Char()
    book_id = fields.Many2one('lib.book')
    subscriber = fields.Char()
    serialnumber = fields.Integer()
    Issuerequestdate = fields.Date()
    # status =fields.Selection([('draff','Draff'),('issued','Issued'),('return','Return')],default='draff')

    status = fields.Selection([
        ('draff' , 'Draff'),
        ('issued' , 'Issued'),
        ('return' , 'Return')], default = 'draff')

    state = fields.Selection([
        ('issue' , 'Issue'),
        ('request:issue' , 'Request:Issue'),
        ('cancle' , 'Cancle')])

    def action_issue(self) :
        for record in self :
             if record.state == 'cancle':
                raise UserError ("Cancle book cannot be issue")
             record.state = 'issue'

    def action_request_issue(self):
        for record in self:
            record.state = 'request:issue'

    def action_cancle(self):
        for record in self:
             if record.state == 'issue':
                 raise UserError ("issue book cannot be cancle")
             record.state = 'cancle'


    class BookStock(models.Model):
        _name = "book.stock"
        _description ="Book Stock"

