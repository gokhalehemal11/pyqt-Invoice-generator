# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import MySQLdb
from MySQLdb import Error

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):

    def __init__(self):
        self.total= 0.0
        self.grand_total= 0.0
        try:
            self.con = MySQLdb.connect(host="localhost",user="root",passwd="pccoe",db="invoice_system")

            if (self.con.open):
                print ("connected")
                self.cur = self.con.cursor()
                q = " select count(invoice_id) from invoices"
                self.cur.execute(q)
                res = self.cur.fetchone()
                self.invoice_id= int(res[0]) + 1
                q2 = " select invoice_id from invoices"
                self.cur.execute(q2)
                res2 = self.cur.fetchall()
                self.all_past_invoice_ids= [int(i[0]) for i in res2]
            else:
                print ("Not connected")

        except Error as e:
            print(e)

    def reset_all(self):
        self.tableWidget.setRowCount(0)
        self.lineEdit_6.setText("0")
        self.lineEdit_8.setText("0")
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")

    def showdialog(self):
        self.msg.exec_()


    def print_previous(self):
        cur_sel= self.qcombobox.currentText()
        if(cur_sel != 'Select Bill'):
            q3 = " select client_name, total_amount, timestamp from invoices where invoice_id = '%d'" % (int(cur_sel))
            self.cur.execute(q3)
            res3 = self.cur.fetchone()
            #print(res3)
            output= ''' 
            <html>
            <head>
            <meta charset="utf-8">
            <style>
              /* reset */
            *
            {
              border: 0;
              box-sizing: content-box;
              color: inherit;
              font-family: inherit;
              font-size: inherit;
              font-style: inherit;
              font-weight: inherit;
              line-height: inherit;
              list-style: none;
              margin: 0;
              padding: 0;
              text-decoration: none;
              vertical-align: top;
            }

            /* content editable */

            *] { border-radius: 0.25em; min-width: 1em; outline: 0; }

            *] { cursor: pointer; }

            *]:hover, *]:focus, td:hover *], td:focus *], img.hover { background: #DEF; box-shadow: 0 0 1em 0.5em #DEF; }

            span] { display: inline-block; }

            /* heading */

            h1 { font: bold 100% sans-serif; letter-spacing: 0.5em; text-align: center; text-transform: uppercase; }

            /* table */

            table { font-size: 75%; table-layout: fixed; width: 100%; }
            table { border-collapse: separate; border-spacing: 2px; }
            th, td { border-width: 1px; padding: 0.5em; position: relative; text-align: left; }
            th, td { border-radius: 0.25em; border-style: solid; }
            th { background: #EEE; border-color: #BBB; }
            td { border-color: #DDD; }

            /* page */

            html { font: 16px/1 'Open Sans', sans-serif; overflow: auto; padding: 0.5in; }
            html { background: #999; cursor: default; }

            body { box-sizing: border-box; height: 11in; margin: 0 auto; overflow: hidden; padding: 0.5in; width: 8.5in; }
            body { background: #FFF; border-radius: 1px; box-shadow: 0 0 1in -0.25in rgba(0, 0, 0, 0.5); }

            /* header */

            header { margin: 0 0 3em; }
            header:after { clear: both; content: ""; display: table; }

            header h1 { background: #000; border-radius: 0.25em; color: #FFF; margin: 0 0 1em; padding: 0.5em 0; }
            header address { float: left; font-size: 75%; font-style: normal; line-height: 1.25; margin: 0 1em 1em 0; }
            header address p { margin: 0 0 0.25em; }
            header span, header img { display: block; float: right; }
            header span { margin: 0 0 1em 1em; max-height: 25%; max-width: 60%; position: relative; }
            header img { max-height: 100%; max-width: 100%; }
            header input { cursor: pointer; -ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=0)"; height: 100%; left: 0; opacity: 0; position: absolute; top: 0; width: 100%; }

            /* article */

            article, article address, table.meta, table.inventory { margin: 0 0 3em; }
            article:after { clear: both; content: ""; display: table; }
            article h1 { clip: rect(0 0 0 0); position: absolute; }

            article address { float: left; font-size: 125%; font-weight: bold; }

            /* table meta & balance */

            table.meta, table.balance { float: right; width: 36%; }
            table.meta:after, table.balance:after { clear: both; content: ""; display: table; }

            /* table meta */

            table.meta th { width: 40%; }
            table.meta td { width: 60%; }

            /* table items */

            table.inventory { clear: both; width: 100%; }
            table.inventory th { font-weight: bold; text-align: center; }

            table.inventory td:nth-child(1) { width: 26%; }
            table.inventory td:nth-child(2) { width: 38%; }
            table.inventory td:nth-child(3) { text-align: right; width: 12%; }
            table.inventory td:nth-child(4) { text-align: right; width: 12%; }
            table.inventory td:nth-child(5) { text-align: right; width: 12%; }

            /* table balance */

            table.balance th, table.balance td { width: 50%; }
            table.balance td { text-align: right; }

            /* aside */

            aside h1 { border: none; border-width: 0 0 1px; margin: 0 0 1em; }
            aside h1 { border-color: #999; border-bottom-style: solid; }

            @media print {
              * { -webkit-print-color-adjust: exact; }
              html { background: none; padding: 0; }
              body { box-shadow: none; margin: 0; }
              span:empty { display: none; }
              .add, .cut { display: none; }
            }

            @page { margin: 0; }
            </style>
            <title>Invoice</title>
            </head>
            <body>
            <header>
            <h1>Tax Invoice</h1>
            <address>
            <b><p>CHEMITECH INDUSTRIES</p></b>
            <p>Survey No. 164/A, Nigdi Talawade Road,<br>Talawade, Pune - 411 062</p>
            <p>Mob. : 9422304951 / 8446357726, <br>Email : chemitechindustries@gmail.com</p>
            <p><b>GSTIN : 27EXJPP7938C1ZZ</b></p>
            </address>
            </header>
            <article>
            <address>
            <p>To<br>'''+ str(res3[0])+'''</p>
            </address>
            <table class="meta">
            <tr>
            <th><span>Invoice #</span></th>
            <td><span>'''+cur_sel+'''</span></td>
            </tr>
            <tr>
            <th><span>Date</span></th>
            <td><span>'''+str(res3[2])+'''</span></td>
            </tr>
            <tr>
            <th><span>Amount</span></th>
            <td><span id="prefix">Rs </span><span>'''+str(res3[1])+''' /-</span></td>
            </tr>
            </table>
            <table class="inventory">
            <thead>
            <tr>
            <th><span>Item</span></th>
            <th><span>Description</span></th>
            <th><span>Rate</span></th>
            <th><span>Quantity</span></th>
            </tr>
            </thead>
            <tbody>'''
            q4 = " select product_name, product_price, product_qty, product_desc from individual_invoice_details where id = '%d'" % (int(cur_sel))
            self.cur.execute(q4)
            res4 = self.cur.fetchall()
            print(res4)
            for r in res4:
                output+='''
                <tr>
                <td><span>'''+str(r[0])+'''</span></td>
                <td><span>'''+str(r[3])+'''</span></td>
                <td><span data-prefix>Rs </span><span>'''+str(r[1])+'''</span></td>
                <td><span>'''+str(r[2])+'''</span></td>
                </tr>'''
            output+= '''</tbody>
            </table>
            <table class="balance">
            <tr>
            <th><span>Grand Total</span></th>
            <td><span data-prefix>Rs </span><span>'''+str(res3[1])+''' /-</span></td>
            </tr>
            </table>
            </article>
            <aside>
            <h1><span>Bank Details</span></h1>
            <div>
            <table class="inventory">
            <tr>
            <th><span>Bank Name</span></th>
            <td><span data-prefix></span><span>Syndicate Bank</span></td>
            </tr>
            <tr>
            <th><span>Branch</span></th>
            <td><span data-prefix></span><span>Chikhali, Pune - 412 114</span></td>
            </tr>
            <tr>
            <th><span>A/c No.</span></th>
            <td><span data-prefix></span><span>53351010006786</span></td>
            </tr>
            <tr>
            <th><span>IFSC</span></th>
            <td><span data-prefix></span><span>SYNB0005335</span></td>
            </tr>
            </table>
            <p>I/We hereby certify that my/our Registration Certificate under the GST Act, 2017 is in force on the date on which the supply of goods specified in this tax invoice is made by me/us and that the transaction of supplies covered by this tax invoice has been effected by me/us and it shall be accounted for in the turnover of sales while filing of return and the due tax, if any, payable on the sale has been paid or shall be paid. Certified that the particulars given above are true and correct to the amount indicated represents the price actually charged and that there is no flow of additional consideration directly or indirectly from buyer. </p>
            <table class="balance">
            <tr>
            <th><span>Receiver's Signature</span></th>
            <td><span data-prefix></span><span></span></td>
            </tr>
            <tr>
            <th><span>For CHEMITECH INDUSTRIES</span></th>
            <td><span data-prefix></span><span></span></td>
            </tr>
            </table>
            </div>
            </aside>
            </body>
            </html>
            '''
            filename= str(cur_sel)+'_'+str(res3[0])+'_'+str(res3[2])+'.html'
            file= open('previous_searched/'+filename,'w')
            file.write(output)
            file.close()
            webbrowser.open_new_tab('file:///'+os.getcwd()+'/previous_searched/' + filename)
        else:
            self.msg.setInformativeText("Please select Invoice No.")
            self.msg.setWindowTitle("Empty Selection")
            self.showdialog()


    def get_values_from_table(self):
        client= self.lineEdit_5.text()
        if(client == ""):
            self.msg.setInformativeText("Client Name cannot be empty")
            self.msg.setWindowTitle("Empty Client Name")
            self.showdialog()
        else:
            output= ''' 
            <html>
            <head>
            <meta charset="utf-8">
            <style>
              /* reset */
            *
            {
              border: 0;
              box-sizing: content-box;
              color: inherit;
              font-family: inherit;
              font-size: inherit;
              font-style: inherit;
              font-weight: inherit;
              line-height: inherit;
              list-style: none;
              margin: 0;
              padding: 0;
              text-decoration: none;
              vertical-align: top;
            }

            /* content editable */

            *] { border-radius: 0.25em; min-width: 1em; outline: 0; }

            *] { cursor: pointer; }

            *]:hover, *]:focus, td:hover *], td:focus *], img.hover { background: #DEF; box-shadow: 0 0 1em 0.5em #DEF; }

            span] { display: inline-block; }

            /* heading */

            h1 { font: bold 100% sans-serif; letter-spacing: 0.5em; text-align: center; text-transform: uppercase; }

            /* table */

            table { font-size: 75%; table-layout: fixed; width: 100%; }
            table { border-collapse: separate; border-spacing: 2px; }
            th, td { border-width: 1px; padding: 0.5em; position: relative; text-align: left; }
            th, td { border-radius: 0.25em; border-style: solid; }
            th { background: #EEE; border-color: #BBB; }
            td { border-color: #DDD; }

            /* page */

            html { font: 16px/1 'Open Sans', sans-serif; overflow: auto; padding: 0.5in; }
            html { background: #999; cursor: default; }

            body { box-sizing: border-box; height: 11in; margin: 0 auto; overflow: hidden; padding: 0.5in; width: 8.5in; }
            body { background: #FFF; border-radius: 1px; box-shadow: 0 0 1in -0.25in rgba(0, 0, 0, 0.5); }

            /* header */

            header { margin: 0 0 3em; }
            header:after { clear: both; content: ""; display: table; }

            header h1 { background: #000; border-radius: 0.25em; color: #FFF; margin: 0 0 1em; padding: 0.5em 0; }
            header address { float: left; font-size: 75%; font-style: normal; line-height: 1.25; margin: 0 1em 1em 0; }
            header address p { margin: 0 0 0.25em; }
            header span, header img { display: block; float: right; }
            header span { margin: 0 0 1em 1em; max-height: 25%; max-width: 60%; position: relative; }
            header img { max-height: 100%; max-width: 100%; }
            header input { cursor: pointer; -ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=0)"; height: 100%; left: 0; opacity: 0; position: absolute; top: 0; width: 100%; }

            /* article */

            article, article address, table.meta, table.inventory { margin: 0 0 3em; }
            article:after { clear: both; content: ""; display: table; }
            article h1 { clip: rect(0 0 0 0); position: absolute; }

            article address { float: left; font-size: 125%; font-weight: bold; }

            /* table meta & balance */

            table.meta, table.balance { float: right; width: 36%; }
            table.meta:after, table.balance:after { clear: both; content: ""; display: table; }

            /* table meta */

            table.meta th { width: 40%; }
            table.meta td { width: 60%; }

            /* table items */

            table.inventory { clear: both; width: 100%; }
            table.inventory th { font-weight: bold; text-align: center; }

            table.inventory td:nth-child(1) { width: 26%; }
            table.inventory td:nth-child(2) { width: 38%; }
            table.inventory td:nth-child(3) { text-align: right; width: 12%; }
            table.inventory td:nth-child(4) { text-align: right; width: 12%; }
            table.inventory td:nth-child(5) { text-align: right; width: 12%; }

            /* table balance */

            table.balance th, table.balance td { width: 50%; }
            table.balance td { text-align: right; }

            /* aside */

            aside h1 { border: none; border-width: 0 0 1px; margin: 0 0 1em; }
            aside h1 { border-color: #999; border-bottom-style: solid; }

            @media print {
              * { -webkit-print-color-adjust: exact; }
              html { background: none; padding: 0; }
              body { box-shadow: none; margin: 0; }
              span:empty { display: none; }
              .add, .cut { display: none; }
            }

            @page { margin: 0; }
            </style>
            <title>Invoice</title>
            </head>
            <body>
            <header>
            <h1>Tax Invoice</h1>
            <address>
            <b><p>CHEMITECH INDUSTRIES</p></b>
            <p>Survey No. 164/A, Nigdi Talawade Road,<br>Talawade, Pune - 411 062</p>
            <p>Mob. : 9422304951 / 8446357726, <br>Email : chemitechindustries@gmail.com</p>
            <p><b>GSTIN : 27EXJPP7938C1ZZ</b></p>
            </address>
            </header>
            <article>
            <address>
            <p>To<br>'''+ client+'''</p>
            </address>
            <table class="meta">
            <tr>
            <th><span>Invoice #</span></th>
            <td><span>'''+str(self.invoice_id)+'''</span></td>
            </tr>
            <tr>
            <th><span>Date</span></th>
            <td><span>'''+str(date.today())+'''</span></td>
            </tr>
            <tr>
            <th><span>Amount</span></th>
            <td><span id="prefix">Rs </span><span>'''+str(self.grand_total)+''' /-</span></td>
            </tr>
            </table>
            <table class="inventory">
            <thead>
            <tr>
            <th><span>Item</span></th>
            <th><span>Description</span></th>
            <th><span>Rate</span></th>
            <th><span>Quantity</span></th>
            </tr>
            </thead>
            <tbody>'''
            self.cur.execute('insert into invoices values ("%d" , "%s" , "%s" , "%s" )' % (self.invoice_id , str(client) , str(self.grand_total), str(date.today())))
            self.con.commit()
            allRows = self.tableWidget.rowCount()
            for row in xrange(0,allRows):
                name = self.tableWidget.item(row,0)
                description = self.tableWidget.item(row,1)
                qty = self.tableWidget.item(row,2)
                price = self.tableWidget.item(row,3)
                output+='''
                <tr>
                <td><span>'''+name.text()+'''</span></td>
                <td><span>'''+description.text()+'''</span></td>
                <td><span data-prefix>Rs </span><span>'''+str(price.text())+'''</span></td>
                <td><span>'''+str(qty.text())+'''</span></td>
                </tr>'''
                self.cur.execute('insert into individual_invoice_details values ("%d" , "%s" , "%s" , "%s", "%s" )' % (self.invoice_id , str(name.text()) , str(price.text()), int(qty.text()), str(description.text())))
                self.con.commit()
            output+= '''</tbody>
            </table>
            <table class="balance">
            <tr>
            <th><span>Total</span></th>
            <td><span data-prefix>Rs </span><span>'''+str(self.total)+''' /-</span></td>
            </tr>
            <tr>
            <th><span>CGST (@ 9%) + SGST (@ 9%)</span></th>
            <td><span data-prefix></span><span>18 %</span></td>
            </tr>
            <tr>
            <th><span>Grand Total</span></th>
            <td><span data-prefix>Rs </span><span>'''+str(self.grand_total)+''' /-</span></td>
            </tr>
            </table>
            </article>
            <aside>
            <h1><span>Bank Details</span></h1>
            <div>
            <table class="inventory">
            <tr>
            <th><span>Bank Name</span></th>
            <td><span data-prefix></span><span>Syndicate Bank</span></td>
            </tr>
            <tr>
            <th><span>Branch</span></th>
            <td><span data-prefix></span><span>Chikhali, Pune - 412 114</span></td>
            </tr>
            <tr>
            <th><span>A/c No.</span></th>
            <td><span data-prefix></span><span>53351010006786</span></td>
            </tr>
            <tr>
            <th><span>IFSC</span></th>
            <td><span data-prefix></span><span>SYNB0005335</span></td>
            </tr>
            </table>
            <p>I/We hereby certify that my/our Registration Certificate under the GST Act, 2017 is in force on the date on which the supply of goods specified in this tax invoice is made by me/us and that the transaction of supplies covered by this tax invoice has been effected by me/us and it shall be accounted for in the turnover of sales while filing of return and the due tax, if any, payable on the sale has been paid or shall be paid. Certified that the particulars given above are true and correct to the amount indicated represents the price actually charged and that there is no flow of additional consideration directly or indirectly from buyer. </p>
            <table class="balance">
            <tr>
            <th><span>Receiver's Signature</span></th>
            <td><span data-prefix></span><span></span></td>
            </tr>
            <tr>
            <th><span>For CHEMITECH INDUSTRIES</span></th>
            <td><span data-prefix></span><span></span></td>
            </tr>
            </table>
            </div>
            </aside>
            </body>
            </html>
            '''
            filename= str(self.invoice_id)+'_'+str(client)+'_'+str(date.today())+'.html'
            file= open('output/'+filename,'w')
            file.write(output)
            file.close()
            webbrowser.open_new_tab('file:///'+os.getcwd()+'/output/' + filename)
            self.reset_all()
            self.qcombobox.addItem(str(self.invoice_id))
            self.invoice_id+= 1
            #print name.text()+' '+description.text()+' '+qty.text()+' '+price.text()

    def get_values_from_user(self):
        name = self.lineEdit.text()
        description= self.lineEdit_2.text()
        try:
            qty= int(self.lineEdit_3.text())
            price= float(self.lineEdit_4.text())
        except Exception as e:
            self.msg.setInformativeText("Qty and Price should be numeric")
            self.msg.setWindowTitle("Invalid values")
            self.showdialog()
        tax= 18
        self.total= float(self.lineEdit_6.text())
        self.grand_total= float(self.lineEdit_8.text())
        cur_price= qty*price
        self.total+= cur_price
        self.grand_total= self.total + (self.total*0.18)

        if (name == "" or description =="" or qty=="" or price == ""):
            self.msg.setInformativeText("All fields are necessary")
            self.msg.setWindowTitle("Empty Fields")
            self.showdialog()
        else:
            rowPosition= self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition , 0, QtGui.QTableWidgetItem(name))
            self.tableWidget.setItem(rowPosition , 1, QtGui.QTableWidgetItem(description))
            self.tableWidget.setItem(rowPosition , 2, QtGui.QTableWidgetItem(str(qty)))
            self.tableWidget.setItem(rowPosition , 3, QtGui.QTableWidgetItem(str(price)))
            self.lineEdit_6.setText(_translate("Form", str(self.total), None))
            self.lineEdit_8.setText(_translate("Form", str(self.grand_total), None))
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            #print(name,description,qty,price,client)


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(685, 457)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(570, 420, 97, 27))
        self.pushButton.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 420, 97, 27))
        self.pushButton_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 190, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 190, 251, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(410, 190, 81, 27))
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 190, 61, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 190, 97, 27))
        self.pushButton_3.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(Form)
        self.dateTimeEdit.setReadOnly(True)
        self.dateTimeEdit.setGeometry(QtCore.QRect(480, 10, 194, 27))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 170, 101, 17))
        self.label.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(210, 170, 141, 17))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(430, 170, 31, 17))
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(510, 170, 41, 17))
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(380, 110, 21, 21))
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_5 = QtGui.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(410, 110, 241, 27))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(480, 90, 111, 17))
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(30, 230, 611, 111))
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.lineEdit_6 = QtGui.QLineEdit(Form)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(480, 350, 113, 27))
        self.lineEdit_6.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(Form)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QtCore.QRect(600, 350, 61, 27))
        self.lineEdit_7.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(Form)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setGeometry(QtCore.QRect(480, 380, 131, 27))
        self.lineEdit_8.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(400, 350, 71, 31))
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(390, 380, 111, 31))
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(620, 380, 31, 21))
        self.label_9.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.msg = QtGui.QMessageBox()
        self.msg.setIcon(QtGui.QMessageBox.Warning)
        self.msg.setText("Alert")
        self.msg.setStandardButtons(QtGui.QMessageBox.Ok)
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(40, 20, 301, 61))
        self.label_10.setStyleSheet(_fromUtf8("font: 75 20pt \"Ubuntu\";\n"
"color: rgb(0, 0, 0);"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(60, 70, 341, 31))
        self.label_11.setStyleSheet(_fromUtf8("font: 75 oblique 9pt \"Umpush\";"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.graphicsView = QtGui.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(30, 20, 311, 91))
        self.graphicsView.setStyleSheet(_fromUtf8("background-color: rgb(229, 229, 229);"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label_12 = QtGui.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(70, 370, 131, 17))
        self.label_12.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 390, 51, 27))
        self.pushButton_4.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.qcombobox = QtGui.QComboBox(Form)
        self.qcombobox.setGeometry(QtCore.QRect(80, 390, 100, 27))
        self.qcombobox.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.qcombobox.setObjectName(_fromUtf8("qcombobox"))
        self.qcombobox.addItem("Select Bill")
        for id in self.all_past_invoice_ids:
            self.qcombobox.addItem(str(id))
        self.label_10.raise_()
        self.label_11.raise_()

        self.pushButton_3.clicked.connect(self.get_values_from_user)
        self.pushButton.clicked.connect(self.get_values_from_table)
        self.pushButton_2.clicked.connect(self.reset_all)
        self.pushButton_4.clicked.connect(self.print_previous)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Invoice Generator", None))
        self.pushButton.setText(_translate("Form", "Generate Bill", None))
        self.pushButton_2.setText(_translate("Form", "Reset", None))
        self.pushButton_3.setText(_translate("Form", "Add Item", None))
        self.label.setText(_translate("Form", "Product Name", None))
        self.label_2.setText(_translate("Form", "Product Description", None))
        self.label_3.setText(_translate("Form", " Qty", None))
        self.label_4.setText(_translate("Form", "Price", None))
        self.label_5.setText(_translate("Form", "To:", None))
        self.label_6.setText(_translate("Form", "Client Name", None))
        self.label_7.setText(_translate("Form", "Total + Tax", None))
        self.label_8.setText(_translate("Form", "Grand Total", None))
        self.lineEdit_7.setWhatsThis(_translate("Form", "Tax rate", None))
        self.lineEdit_7.setText(_translate("Form", "18 %", None))
        self.lineEdit_6.setText(_translate("Form", "0", None))
        self.lineEdit_8.setText(_translate("Form", "0", None))
        self.label_9.setText(_translate("Form", "Rs", None))
        self.label_10.setText(_translate("Form", "CHEMITECH INDUSTRIES", None))
        self.label_11.setText(_translate("Form", "EXPERT IN ALL TYPES OF ELECTRO PLATING", None))
        self.label_12.setText(_translate("Form", "Search Past Invoice", None))
        self.pushButton_4.setText(_translate("Form", "Print", None))


if __name__ == "__main__":
    import sys
    from datetime import date
    import webbrowser, os
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

