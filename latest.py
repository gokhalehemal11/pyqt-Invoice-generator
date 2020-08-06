# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb
from MySQLdb import Error

class Ui_Form(object):
    def __init__(self):
        self.total= 0.0
        self.grand_total= 0.0
        self.cgst= 0.09
        self.sgst= 0.09
        self.cgst_total= 0.0
        self.sgst_total= 0.0
        self.actual_thick= ""
        try:
            self.con = MySQLdb.connect(host="13.235.81.57",user="remote",passwd="Remote@Pass_123",db="invoice_system")
            #self.con = MySQLdb.connect(host="localhost",user="root",passwd="pccoe",db="invoice_system")

            if (self.con.open):
                print ("connected")
                try:
                    self.cur = self.con.cursor()
                    q = " select invoice_id from invoices order by invoice_id desc limit 1"
                    self.cur.execute(q)
                    res = self.cur.fetchone()
                    self.invoice_id= int(res[0]) + 1
                    q2 = " select invoice_id from invoices"
                    self.cur.execute(q2)
                    res2 = self.cur.fetchall()
                    self.all_past_invoice_ids= [str(i[0]) for i in res2]
                    q3 = " select client_name, gst_no from invoices"
                    self.cur.execute(q3)
                    res3 = self.cur.fetchall()
                    self.all_clients= [str(i[0]) for i in res3]
                    self.all_gst= [str(i[1]) for i in res3]
                    q4 = " select product_name from individual_invoice_details"
                    self.cur.execute(q4)
                    res4 = self.cur.fetchall()
                    self.all_past_part_nos= [str(i[0]) for i in res4]
                except Exception as e:
                    print(e)
            else:
                print ("Not connected")

        except Error as e:
            print (e)

    def reset_all(self):
        self.tableWidget.setRowCount(0)
        self.part_no.setText("")
        self.part_desc.setText("")
        self.qty.setText("")
        self.rate.setText("")
        self.lot_no.setText("")
        self.actual.setText("")
        self.specified.setText("")
        self.obs1.setText("")
        self.obs2.setText("")
        self.obs3.setText("")
        self.obs4.setText("")
        self.sac.setText("")
        self.cgst_tot.setText("0")
        self.sgst_tot.setText("0")
        self.tot.setText("0")
        self.grand_tot.setText("0")

    def showdialog(self):
        self.msg.exec_()

    def get_values_from_table(self):
        client= self.client.text()
        gst_no= self.gst.text()
        cur_date= str(date.today())
        allRows = self.tableWidget.rowCount()
        if(client == "" or gst_no == ""):
            self.msg.setInformativeText("Client Name and GST No. cannot be empty")
            self.msg.setWindowTitle("Empty Fields")
            self.showdialog()
        elif(allRows <= 1):
            self.msg.setInformativeText("All fields are necessary")
            self.msg.setWindowTitle("Empty Fields")
            self.showdialog()
        else:
            self.cur.execute('insert into invoices values ("%d" , "%s" , "%s", "%s" , "%s" )' % (self.invoice_id , str(client) , str(gst_no), str(self.grand_total), str(date.today())))
            self.con.commit()
            tc_output= '''
            <html>
               <head>
                  <meta charset="utf-8">
                  <link rel="stylesheet" type="text/css" href="../static/css/TC.css">
                  <title>Test Certificate</title>
               </head>
               <body>
                  <header>
                     <h1>Plating Test Certificate</h1>
                     <img src="../static/logo.png">
                     <address>
                        <b>
                           <p>CHEMITECH INDUSTRIES</p>
                        </b>
                        <p>Survey No. 164/A, Nigdi Talawade Road,<br>Talawade, Pune - 411 062</p>
                        <p>Mob. : 8446357726 / 9422304951, <br>Email : chemitechindustries@gmail.com</p>
                        <p><b>GSTIN : 27EXJPP7938C1ZZ</b></p>
                     </address>
                  </header>
                  <article>
                     <h2>To: '''+str(client)+'''</h2>
                     <h2>GSTIN: '''+str(gst_no)+'''</h2>
                     <br>
                     <table class="tg" style="undefined;table-layout: fixed; width: 1577px">
                        <colgroup>
                           <col style="width: 106px">
                           <col style="width: 454px">
                           <col style="width: 274px">
                           <col style="width: 286px">
                           <col style="width: 81px">
                           <col style="width: 94px">
                           <col style="width: 46px">
                           <col style="width: 48px">
                           <col style="width: 94px">
                           <col style="width: 94px">
                        </colgroup>
                        <thead>
                           <tr>
                              <th class="tg-0lax" colspan="2">&nbsp;&nbsp;&nbsp;<br>TC. No. &nbsp;&nbsp;&nbsp;'''+str(self.invoice_id)+''' </th>
                              <th class="tg-0lax" colspan="2">&nbsp;&nbsp;&nbsp;<br>TC. Date &nbsp;&nbsp;&nbsp;'''+cur_date+''' </th>
                              <th class="tg-0lax" colspan="3">&nbsp;&nbsp;&nbsp;<br>Ch. No.: &nbsp;&nbsp;&nbsp;'''+str(self.invoice_id)+''' </th>
                              <th class="tg-0lax" colspan="3">&nbsp;&nbsp;&nbsp;<br>Ch. Date: &nbsp;&nbsp;&nbsp;'''+cur_date+'''</th>
                           </tr>
                        </thead>
                        <tbody>
                           <tr>
                              <td class="tg-0lax" rowspan="2">&nbsp;&nbsp;&nbsp;<br>Sr.No.&nbsp;&nbsp;&nbsp;</td>
                              <td class="tg-0lax" rowspan="2">&nbsp;&nbsp;&nbsp;<br>Part Description&nbsp;&nbsp;&nbsp;</td>
                              <td class="tg-0lax" rowspan="2">&nbsp;&nbsp;&nbsp;<br>Part No.&nbsp;&nbsp;&nbsp;</td>
                              <td class="tg-0lax" rowspan="2">&nbsp;&nbsp;&nbsp;<br>Quantity<br>&nbsp;&nbsp;&nbsp;<br>Nos./Kg.&nbsp;&nbsp;&nbsp;</td>
                              <td class="tg-0lax" colspan="6">&nbsp;&nbsp;&nbsp;<br>Actual Plating Thickness: &nbsp;&nbsp;&nbsp;'''+str(self.actual_thick)+'''</td>
                           </tr>
                           <tr>
                              <td class="tg-0lax">&nbsp;&nbsp;&nbsp;<br>Specified&nbsp;&nbsp;&nbsp;</td>
                              <td class="tg-0lax">&nbsp;&nbsp;&nbsp;<br>Observed 1&nbsp;&nbsp;&nbsp;</td>
                              <td class="tg-0lax" colspan="2">&nbsp;&nbsp;&nbsp;<br>Observed 2&nbsp;&nbsp;&nbsp;</td>
                              <td class="tg-0lax">&nbsp;&nbsp;&nbsp;<br>Observed 3&nbsp;&nbsp;&nbsp;</td>
                              <td class="tg-0lax">&nbsp;&nbsp;&nbsp;<br>Observed 4&nbsp;&nbsp;&nbsp;</td>
                           </tr>
            '''
            invoice_output= '''
            <html>
               <head>
                  <meta charset="utf-8">
                  <link rel="stylesheet" type="text/css" href="../static/css/invoice.css">
                  <title>Invoice</title>
               </head>
               <body>
                  <header>
                     <h1>Tax Invoice</h1>
                     <img src="../static/logo.png">
                     <address>
                        <b>
                           <p>CHEMITECH INDUSTRIES</p>
                        </b>
                        <p>Survey No. 164/A, Nigdi Talawade Road,<br>Talawade, Pune - 411 062</p>
                        <p>Mob. : 8446357726 / 9422304951, <br>Email : chemitechindustries@gmail.com</p>
                        <p><b>GSTIN : 27EXJPP7938C1ZZ</b></p>
                     </address>
                  </header>
                  <article>
                     <address>
                        <p>To: '''+str(client)+'''<br>GSTIN: '''+str(gst_no)+'''</p>
                     </address>
                     <table class="meta">
                        <tr>
                           <th><span>Invoice #</span></th>
                           <td><span>'''+str(self.invoice_id)+'''</span></td>
                        </tr>
                        <tr>
                           <th><span>Date</span></th>
                           <td><span>'''+cur_date+'''</span></td>
                        </tr>
                        <tr>
                           <th><span>D. Challan No.</span></th>
                           <td><span>'''+str(self.invoice_id)+'''</span></td>
                        </tr>
                        <tr>
                           <th><span>Date</span></th>
                           <td><span>'''+cur_date+'''</span></td>
                        </tr>
                        <tr>
                           <th><span>P.O No.</span></th>
                           <td><span></span></td>
                        </tr>
                        <tr>
                           <th><span>Date</span></th>
                           <td><span></span></td>
                        </tr>
                        <tr>
                           <th><span>Vendor Code No.</span></th>
                           <td><span></span></td>
                        </tr>
                     </table>
                     <table class="inventory">
                        <thead>
                           <tr>
                              <th><span>Item</span></th>
                              <th><span>Description</span></th>
                              <th><span>HSN /<br>SAC Code</span></th>
                              <th><span>Quantity</span></th>
                              <th><span>Rate</span></th>
                              <th><span>Amount</span></th>
                           </tr>
                        </thead>
                        <tbody>
            '''
            del_output= '''
            <html>
               <head>
                  <meta charset="utf-8">
                  <link rel="stylesheet" type="text/css" href="../static/css/del_chalan.css">
                  <title>Delivery Chalan</title>
               </head>
               <body>
                  <header>
                     <h1>Delivery Chalan</h1>
                     <img src="../static/logo.png">
                     <address>
                        <b>
                           <p>CHEMITECH INDUSTRIES</p>
                        </b>
                        <p>Survey No. 164/A, Nigdi Talawade Road,<br>Talawade, Pune - 411 062</p>
                        <p>Mob. : 8446357726 / 9422304951, <br>Email : chemitechindustries@gmail.com</p>
                        <p><b>GSTIN : 27EXJPP7938C1ZZ</b></p>
                     </address>
                  </header>
                  <article>
                     <address>
                        <p>To: '''+str(client)+'''<br>GSTIN: '''+str(gst_no)+'''</p>
                     </address>
                     <table class="meta">
                        <tr>
                           <th><span>Invoice #</span></th>
                           <td><span>'''+str(self.invoice_id)+'''</span></td>
                        </tr>
                        <tr>
                           <th><span>Date</span></th>
                           <td><span>'''+cur_date+'''</span></td>
                        </tr>
                        <tr>
                           <th><span>D. Challan No.</span></th>
                           <td><span>'''+str(self.invoice_id)+'''</span></td>
                        </tr>
                        <tr>
                           <th><span>Date</span></th>
                           <td><span>'''+cur_date+'''</span></td>
                        </tr>
                        <tr>
                           <th><span>P.O No.</span></th>
                           <td><span></span></td>
                        </tr>
                        <tr>
                           <th><span>Date</span></th>
                           <td><span></span></td>
                        </tr>
                        <tr>
                           <th><span>Vendor Code No.</span></th>
                           <td><span></span></td>
                        </tr>
                     </table>
                     <table class="inventory">
                        <thead>
                           <tr>
                              <th><span>Item</span></th>
                              <th><span>Description</span></th>
                              <th><span>Quantity</span></th>
                              <th><span>Remarks</span></th>
                           </tr>
                        </thead>
                        <tbody>
            '''
            for row in xrange(1,allRows):
                pid = self.tableWidget.item(row,0)
                self.all_past_part_nos.append(pid)
                description = self.tableWidget.item(row,1)
                qty = self.tableWidget.item(row,2)
                price = self.tableWidget.item(row,3)
                lot_no = self.tableWidget.item(row,4)
                specified = self.tableWidget.item(row,5)
                obs1 = self.tableWidget.item(row,6)
                obs2 = self.tableWidget.item(row,7)
                obs3 = self.tableWidget.item(row,8)
                obs4 = self.tableWidget.item(row,9)
                sac = self.tableWidget.item(row,10)
                amount= float(qty.text())*float(price.text())
                amount= round(amount, 2)
                self.cur.execute('insert into individual_invoice_details values ("%d" , "%s" , "%s" , "%s", "%s", "%s" )' % (self.invoice_id , str(pid.text()) , str(price.text()), int(qty.text()), str(description.text()), str(sac.text())))
                self.con.commit()
                tc_output+='''
                <tr>
                  <td class="tg-0lax">&nbsp;&nbsp;&nbsp;<br>'''+str(row)+''' &nbsp;&nbsp;&nbsp;</td>
                  <td class="tg-0lax">&nbsp;&nbsp;&nbsp;<br>'''+str(description.text())+''' &nbsp;&nbsp;&nbsp;</td>
                  <td class="tg-0lax">&nbsp;&nbsp;&nbsp;<br>'''+str(pid.text())+''' &nbsp;&nbsp;&nbsp;</td>
                  <td class="tg-0lax">&nbsp;&nbsp;&nbsp;<br>'''+str(qty.text())+'''&nbsp;&nbsp;&nbsp;</td>
                  <td class="tg-0lax">&nbsp;&nbsp;&nbsp;<br>'''+str(specified.text())+'''&nbsp;&nbsp;&nbsp;</td>
                  <td class="tg-0lax">&nbsp;&nbsp;&nbsp;<br>'''+str(obs1.text())+''' &nbsp;&nbsp;&nbsp;</td>
                  <td class="tg-0lax" colspan="2">&nbsp;&nbsp;&nbsp;<br>'''+str(obs2.text())+''' &nbsp;&nbsp;&nbsp;</td>
                  <td class="tg-0lax">&nbsp;&nbsp;&nbsp;<br>'''+str(obs3.text())+''' &nbsp;&nbsp;&nbsp;</td>
                  <td class="tg-0lax">&nbsp;&nbsp;&nbsp;<br> '''+str(obs4.text())+'''&nbsp;&nbsp;&nbsp;</td>
               </tr>
                '''
                invoice_output+='''
                <tr>
                  <td><span>'''+str(pid.text())+'''</span></td>
                  <td><span>'''+str(description.text())+'''</span></td>
                  <td>'''+str(sac.text())+'''</td>
                  <td><span>'''+str(qty.text())+'''</span></td>
                  <td><span data-prefix>Rs </span><span>'''+str(price.text())+'''</span></td>
                  <td><span data-prefix>Rs </span><span>'''+str(amount)+'''</span></td>
               </tr>                
                '''
                del_output+='''
                <tr>
                  <td><span>'''+str(pid.text())+'''</span></td>
                  <td><span>'''+str(description.text())+'''</span></td>
                  <td>'''+str(qty.text())+'''</td>
                  <td><span></span></td>
               </tr>
                '''
                #print (pid.text()+' '+description.text()+' '+qty.text()+' '+price.text()+' '+lot_no.text()+' '+specified.text()+' '+obs1.text()+' '+obs2.text()+' '+obs3.text()+' '+obs4.text()+' '+sac.text())
            tc_output+='''<tr>
                              <td class="tg-0lax" colspan="4">   <br>VISUAL : FREE FROM BLACK / WHITE SPOTS                                                                       :                                                   OK   / NOT OK<br>   <br>                UNIFORM COLOURING                                                                       :                                                                         OK   / NOT OK   </td>
                              <td class="tg-0lax" colspan="6">&nbsp;&nbsp;&nbsp;<br>For CHEMITECH&nbsp;&nbsp;&nbsp;INDUSTRIES<br>&nbsp;&nbsp;&nbsp;<br> <br>&nbsp;&nbsp;&nbsp;<br> <br>&nbsp;&nbsp;&nbsp;<br>Authorised Signatory&nbsp;&nbsp;&nbsp;</td>
                           </tr>
                        </tbody>
                     </table>
                  </article>
               </body>
            </html>'''
            invoice_output+='''
            </tbody>
             </table>
             <table class="balance">
                <tr>
                   <th><span>Total</span></th>
                   <td><span data-prefix>Rs </span><span>'''+str(self.total)+''' /-</span></td>
                </tr>
                <tr>
                   <th><span>CGST (@ 9%)</span></th>
                   <td><span data-prefix>Rs </span><span>'''+str(self.cgst_total)+''' /-</span></td>
                </tr>
                <tr>
                   <th><span>SGST (@ 9%)</span></th>
                   <td><span data-prefix>Rs </span><span>'''+str(self.sgst_total)+''' /-</span></td>
                </tr>
                <tr>
                   <th><span>Grand Total</span></th>
                   <td><span data-prefix>Rs </span><span>'''+str(self.grand_total)+''' /-</span></td>
                </tr>
             </table>
             <div>
             <table class="balance" style="float: left;">
                <tr>
                   <th><span>Bank Name</span></th>
                   <td style="width: 70%;"><span data-prefix></span><span>Syndicate Bank</span></td>
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
          </article>
          <table class="tg">
             <thead>
                <tr>
                   <th class="tg-0lax">&nbsp;&nbsp;&nbsp;<br><span style="color:#0D0D0D">I/We&nbsp;&nbsp;&nbsp;hereby certify that my/our Registration Certificate under the GST Act, 2017&nbsp;&nbsp;&nbsp;is in force on the date on which the supply of goods specified in this tax&nbsp;&nbsp;&nbsp;invoice is made by me/us and that the transaction of supplies covered by this&nbsp;&nbsp;&nbsp;tax invoice has been effected by me/us and it shall be accounted for in the&nbsp;&nbsp;&nbsp;turnover of sales while filing of return and the due tax, if any, payable on&nbsp;&nbsp;&nbsp;the sale has been paid or shall be paid.</span><br>&nbsp;&nbsp;&nbsp;<br><span style="color:#0D0D0D">Certified&nbsp;&nbsp;&nbsp;that the particulars given above are true and correct to the amount indicated&nbsp;&nbsp;&nbsp;represents the price actually charged and that there is no flow of additional&nbsp;&nbsp;&nbsp;consideration directly or indirectly from buyer. </span>&nbsp;&nbsp;&nbsp;</th>
                   <th class="tg-0lax">&nbsp;&nbsp;&nbsp;<br> <br>&nbsp;&nbsp;&nbsp;<br> <br>&nbsp;&nbsp;&nbsp;<br> <br>&nbsp;&nbsp;&nbsp;<br><span style="color:#0D0D0D">Receiver's Signature</span>&nbsp;&nbsp;&nbsp;</th>
                   <th class="tg-0lax">&nbsp;&nbsp;&nbsp;<br><span style="color:#0D0D0D">For </span>CHEMITECH INDUSTRIES<br>&nbsp;&nbsp;&nbsp;<br> <br>&nbsp;&nbsp;&nbsp;<br> <br>&nbsp;&nbsp;&nbsp;<br> <br>&nbsp;&nbsp;&nbsp;<br><span style="color:#0D0D0D">Authorised Signatory </span>&nbsp;&nbsp;&nbsp;</th>
                </tr>
                     </thead>
                  </table>
               </body>
            </html>
            '''
            del_output+='''
            </tbody>
                     </table>
                  </article>
                  <table class="tg">
                     <thead>
                        <tr>
                           <th class="tg-0lax">&nbsp;&nbsp;&nbsp;<br><span style="color:#0D0D0D">Received the above material in good&nbsp;&nbsp;&nbsp;condition &amp; order. </span><br>&nbsp;&nbsp;&nbsp;<br> <br>&nbsp;&nbsp;&nbsp;<br> <br>&nbsp;&nbsp;&nbsp;<br> <br>&nbsp;&nbsp;&nbsp;<br><span style="color:#0D0D0D">Receiver’s Signature with stamp</span>&nbsp;&nbsp;&nbsp;</th>
                           <th class="tg-0lax">&nbsp;&nbsp;&nbsp;<br><span style="color:#0D0D0D">For </span>CHEMITECH INDUSTRIES<br>&nbsp;&nbsp;&nbsp;<br> <br>&nbsp;&nbsp;&nbsp;<br> <br>&nbsp;&nbsp;&nbsp;<br> <br>&nbsp;&nbsp;&nbsp;<br><span style="color:#0D0D0D">Authorised Signatory </span>&nbsp;&nbsp;&nbsp;</th>
                        </tr>
                     </thead>
                  </table>
               </body>
            </html>
            '''
            #print(str(self.total)+' '+str(self.cgst_total)+' '+str(self.sgst_total)+' '+str(self.grand_total))
            filename1= str(self.invoice_id)+'_'+str(client)+'_'+cur_date+'.html'
            file= open('Test_Certificate/'+filename1,'w')
            file.write(tc_output)
            file.close()
            filename2= str(self.invoice_id)+'_'+str(client)+'_'+cur_date+'.html'
            file= open('GST_invoice/'+filename2,'w')
            file.write(invoice_output)
            file.close()
            filename3= str(self.invoice_id)+'_'+str(client)+'_'+cur_date+'.html'
            file= open('Delivery_Chalan/'+filename3,'w')
            file.write(del_output)
            file.close()
            self.invoice_id+= 1
            self.all_past_invoice_ids.append(str(self.invoice_id))
            #self.completer = QtWidgets.QCompleter(self.all_past_invoice_ids)
            #self.comboBox.setCompleter(self.completer)
            webbrowser.open_new_tab('file:///'+os.getcwd()+'/Test_Certificate/' + filename1)
            webbrowser.open_new_tab('file:///'+os.getcwd()+'/GST_invoice/' + filename2)
            webbrowser.open_new_tab('file:///'+os.getcwd()+'/Delivery_Chalan/' + filename3)
            self.msg.setInformativeText("Bills Created")
            self.msg.setWindowTitle("Success")
            self.showdialog()
            self.reset_all()
            # print (pid.text()+' '+description.text()+' '+qty.text()+' '+price.text())

    def get_values_from_user(self):
        name = self.part_no.text()          # Part No.
        description= self.part_desc.text()
        lot_no= self.lot_no.text()
        self.actual_thick= self.actual.text()
        specified= self.specified.text()
        obs1= self.obs1.text()
        obs2= self.obs2.text()
        obs3= self.obs3.text()
        obs4= self.obs4.text()
        sac= self.sac.text()
        try:
            qty= int(self.qty.text())
            price= float(self.rate.text())
            self.total= float(self.tot.text())
            self.grand_total= float(self.grand_tot.text())
            cur_price= qty*price
            self.total+= cur_price
            self.total= round(self.total, 2)
            self.cgst_total= round(cur_price * self.cgst,2)
            self.sgst_total= round(cur_price * self.sgst,2)
            self.grand_total= self.total + (self.total*0.18)
            self.grand_total= round(self.grand_total, 2)
        except Exception as e:
            print(e)
            self.msg.setInformativeText("Qty and Price should be numeric")
            self.msg.setWindowTitle("Invalid values")
            self.showdialog()

        if (name == "" or description =="" or qty=="" or price == ""):
            self.msg.setInformativeText("All fields are necessary")
            self.msg.setWindowTitle("Empty Fields")
            self.showdialog()
        else:
            rowPosition= self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(name))
            self.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(description))
            self.tableWidget.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(str(qty)))
            self.tableWidget.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(str(price)))
            self.tableWidget.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(str(lot_no)))
            self.tableWidget.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(str(specified)))
            self.tableWidget.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(str(obs1)))
            self.tableWidget.setItem(rowPosition , 7, QtWidgets.QTableWidgetItem(str(obs2)))
            self.tableWidget.setItem(rowPosition , 8, QtWidgets.QTableWidgetItem(str(obs3)))
            self.tableWidget.setItem(rowPosition , 9, QtWidgets.QTableWidgetItem(str(obs4)))
            self.tableWidget.setItem(rowPosition , 10, QtWidgets.QTableWidgetItem(str(sac)))
            self.tot.setText(str(self.total))
            self.grand_tot.setText(str(self.grand_total))
            self.cgst_tot.setText(str(self.cgst_total))
            self.sgst_tot.setText(str(self.sgst_total))
            self.part_no.setText("")
            self.part_desc.setText("")
            self.qty.setText("")
            self.rate.setText("")
            self.lot_no.setText("")
            self.specified.setText("")
            self.obs1.setText("")
            self.obs2.setText("")
            self.obs3.setText("")
            self.obs4.setText("")
            self.sac.setText("")
            #print(name,description,qty,price,client)
    def print_previous(self):
        cur_sel= self.comboBox.text()
        if(cur_sel != ""):
            q3 = " select client_name, gst_no, total_amount, timestamp from invoices where invoice_id = '%d'" % (int(cur_sel))
            self.cur.execute(q3)
            res3 = self.cur.fetchone()
            #print(res3)
            output= ''' 
            <html>
               <head>
                  <meta charset="utf-8">
                  <link rel="stylesheet" type="text/css" href="../static/css/invoice.css">
                  <title>Invoice</title>
               </head>
               <body>
                  <header>
                     <h1>Tax Invoice</h1>
                     <img src="../static/logo.png">
                     <address>
                        <b>
                           <p>CHEMITECH INDUSTRIES</p>
                        </b>
                        <p>Survey No. 164/A, Nigdi Talawade Road,<br>Talawade, Pune - 411 062</p>
                        <p>Mob. : 8446357726 / 9422304951, <br>Email : chemitechindustries@gmail.com</p>
                        <p><b>GSTIN : 27EXJPP7938C1ZZ</b></p>
                     </address>
            </header>
            <article>
            <address>
            <p>To: '''+ str(res3[0])+'''<br> GSTIN: '''+str(res3[1])+'''</p>
            </address>
            <table class="meta">
            <tr>
            <th><span>Invoice #</span></th>
            <td><span>'''+cur_sel+'''</span></td>
            </tr>
            <tr>
            <th><span>Date</span></th>
            <td><span>'''+str(res3[3])+'''</span></td>
            </tr>
            <tr>
            <th><span>Amount</span></th>
            <td><span id="prefix">Rs </span><span>'''+str(res3[2])+''' /-</span></td>
            </tr>
            </table>
            <table class="inventory">
            <thead>
            <tr>
            <th><span>Item</span></th>
            <th><span>Description</span></th>
            <th><span>HSN / <br>SAC Code</span></th>
            <th><span>Rate</span></th>
            <th><span>Quantity</span></th>
            </tr>
            </thead>
            <tbody>'''
            q4 = " select product_name, product_price, product_qty, product_desc, sac_code from individual_invoice_details where id = '%d'" % (int(cur_sel))
            self.cur.execute(q4)
            res4 = self.cur.fetchall()
            print(res4)
            for r in res4:
                output+='''
                <tr>
                <td><span>'''+str(r[0])+'''</span></td>
                <td><span>'''+str(r[3])+'''</span></td>
                <td><span>'''+str(r[4])+'''</span></td>
                <td><span data-prefix>Rs </span><span>'''+str(r[1])+'''</span></td>
                <td><span>'''+str(r[2])+'''</span></td>
                </tr>'''
            output+= '''</tbody>
            </table>
            <table class="balance">
            <tr>
            <th><span>Grand Total</span></th>
            <td><span data-prefix>Rs </span><span>'''+str(res3[2])+''' /-</span></td>
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
            filename= str(cur_sel)+'_'+str(res3[0])+'_'+str(res3[3])+'.html'
            file= open('previous_searched/'+filename,'w')
            file.write(output)
            file.close()
            webbrowser.open_new_tab('file:///'+os.getcwd()+'/previous_searched/' + filename)
        else:
            self.msg.setInformativeText("Please Enter Invoice No.")
            self.msg.setWindowTitle("Empty Field")
            self.showdialog()

    def autofill_gst(self):
        try:
            client= self.client.text()
            q01 = " select gst_no from invoices where client_name='%s' order by invoice_id desc limit 1" % (str(client))
            self.cur.execute(q01)
            res01 = self.cur.fetchone()
            #print(res01)
            self.gst.setText(res01[0])
        except Exception as e:
            print(e)

    def autofill_client(self):
        try:
            gst= self.gst.text()
            q01 = " select client_name from invoices where gst_no='%s' order by invoice_id desc limit 1" % (str(gst))
            self.cur.execute(q01)
            res01 = self.cur.fetchone()
            #print(res01)
            self.client.setText(res01[0])
        except Exception as e:
            print(e)

    def autofill_part_info(self):
        try:
            p_name= self.part_no.text()
            q01 = " select product_price, product_desc, sac_code from individual_invoice_details where product_name='%s' order by id desc limit 1 " % (str(p_name))
            self.cur.execute(q01)
            res01 = self.cur.fetchone()
            #print(res01)
            self.rate.setText(res01[0])
            self.part_desc.setText(res01[1])
            self.sac.setText(res01[2])
        except Exception as e:
            print(e)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(918, 568)
        Form.setFixedSize(QtCore.QSize(918, 568))
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(50, 60, 301, 21))
        self.label_10.setStyleSheet("font: 20pt \"Ubuntu\";\n""color: rgb(0, 0, 0);\n""")
        self.label_10.setObjectName("label_10")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(680, 420, 41, 31))
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(50, 90, 331, 21))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet("font:  12pt \"Ubuntu\";\n""color: rgb(35, 35, 35);\n""")
        self.label_11.setObjectName("label_11")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 160, 61, 17))
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(60, 440, 171, 17))
        self.label_12.setStyleSheet("color: rgb(0, 0, 0);\n""font: 14pt \"Ubuntu\";")
        self.label_12.setObjectName("label_12")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 470, 81, 31))
        self.pushButton_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        try:
            self.part_no_completer= QtWidgets.QCompleter(self.all_past_part_nos)
        except Exception as e:
            self.part_no_completer= QtWidgets.QCompleter([])
        self.part_no = QtWidgets.QLineEdit(Form)
        self.part_no.setGeometry(QtCore.QRect(20, 180, 113, 27))
        self.part_no.setStyleSheet("color: rgb(0, 0, 0);")
        self.part_no.setObjectName("part_no")
        self.part_no.setCompleter(self.part_no_completer)
        self.part_desc = QtWidgets.QLineEdit(Form)
        self.part_desc.setGeometry(QtCore.QRect(140, 180, 251, 27))
        self.part_desc.setObjectName("part_desc")
        self.qty = QtWidgets.QLineEdit(Form)
        self.qty.setGeometry(QtCore.QRect(400, 180, 81, 27))
        self.qty.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.qty.setObjectName("qty")
        self.rate = QtWidgets.QLineEdit(Form)
        self.rate.setGeometry(QtCore.QRect(490, 180, 61, 27))
        self.rate.setObjectName("rate")
        self.lot_no = QtWidgets.QLineEdit(Form)
        self.lot_no.setGeometry(QtCore.QRect(560, 180, 61, 27))
        self.lot_no.setObjectName("lot_no")
        self.actual = QtWidgets.QLineEdit(Form)
        self.actual.setGeometry(QtCore.QRect(660, 180, 111, 27))
        self.actual.setStyleSheet("color: rgb(0, 0, 0);")
        self.actual.setObjectName("actual")
        self.specified = QtWidgets.QLineEdit(Form)
        self.specified.setGeometry(QtCore.QRect(30, 240, 71, 27))
        self.specified.setObjectName("specified")
        self.obs1 = QtWidgets.QLineEdit(Form)
        self.obs1.setGeometry(QtCore.QRect(130, 240, 71, 27))
        self.obs1.setObjectName("obs1")
        self.obs2 = QtWidgets.QLineEdit(Form)
        self.obs2.setGeometry(QtCore.QRect(230, 240, 71, 27))
        self.obs2.setObjectName("obs2")
        self.obs3 = QtWidgets.QLineEdit(Form)
        self.obs3.setGeometry(QtCore.QRect(330, 240, 71, 27))
        self.obs3.setObjectName("obs3")
        self.obs4 = QtWidgets.QLineEdit(Form)
        self.obs4.setGeometry(QtCore.QRect(440, 240, 71, 27))
        self.obs4.setObjectName("obs4")
        self.sac = QtWidgets.QLineEdit(Form)
        self.sac.setGeometry(QtCore.QRect(550, 240, 111, 27))
        self.sac.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.sac.setObjectName("sac")
        try:
            self.client_completer= QtWidgets.QCompleter(self.all_clients)
        except Exception as e:
            self.client_completer= QtWidgets.QCompleter([])
        self.client = QtWidgets.QLineEdit(Form)
        self.client.setGeometry(QtCore.QRect(630, 80, 241, 27))
        self.client.setObjectName("client")
        self.client.setCompleter(self.client_completer)
        try:
            self.gst_completer= QtWidgets.QCompleter(self.all_gst)
        except Exception as e:
            self.gst_completer= QtWidgets.QCompleter([])
        self.gst = QtWidgets.QLineEdit(Form)
        self.gst.setGeometry(QtCore.QRect(630, 110, 241, 27))
        self.gst.setObjectName("gst")
        self.gst.setCompleter(self.gst_completer)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(230, 160, 91, 17))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(470, 506, 131, 51))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(770, 210, 111, 61))
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(420, 160, 31, 17))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(870, 520, 31, 21))
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(750, 10, 161, 51))
        self.dateTimeEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.dateTimeEdit.setAutoFillBackground(False)
        self.dateTimeEdit.setWrapping(False)
        self.dateTimeEdit.setFrame(True)
        self.dateTimeEdit.setReadOnly(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(500, 160, 41, 17))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(530, 80, 91, 21))
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(326, 506, 131, 51))
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(640, 520, 81, 31))
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.tot = QtWidgets.QLineEdit(Form)
        self.tot.setEnabled(False)
        self.tot.setGeometry(QtCore.QRect(730, 420, 113, 27))
        self.tot.setStyleSheet("color: rgb(0, 0, 0);")
        self.tot.setReadOnly(True)
        self.tot.setObjectName("total")
        self.grand_tot = QtWidgets.QLineEdit(Form)
        self.grand_tot.setEnabled(False)
        self.grand_tot.setGeometry(QtCore.QRect(730, 520, 131, 27))
        self.grand_tot.setStyleSheet("color: rgb(0, 0, 0);")
        self.grand_tot.setReadOnly(True)
        self.grand_tot.setObjectName("grand_total")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(30, 280, 861, 131))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.insertRow(0)
        self.tableWidget.setItem(0 , 0, QtWidgets.QTableWidgetItem("Part No."))
        self.tableWidget.setItem(0 , 1, QtWidgets.QTableWidgetItem("Description"))
        self.tableWidget.setItem(0 , 2, QtWidgets.QTableWidgetItem("Qty"))
        self.tableWidget.setItem(0 , 3, QtWidgets.QTableWidgetItem("Rate"))
        self.tableWidget.setItem(0 , 4, QtWidgets.QTableWidgetItem("Lot No."))
        self.tableWidget.setItem(0 , 5, QtWidgets.QTableWidgetItem("Specified Thickness"))
        self.tableWidget.setItem(0 , 6, QtWidgets.QTableWidgetItem("Observed 1"))
        self.tableWidget.setItem(0 , 7, QtWidgets.QTableWidgetItem("Observed 2"))
        self.tableWidget.setItem(0 , 8, QtWidgets.QTableWidgetItem("Observed 3"))
        self.tableWidget.setItem(0 , 9, QtWidgets.QTableWidgetItem("Observed 4"))
        self.tableWidget.setItem(0 , 10, QtWidgets.QTableWidgetItem("HSN / SAC Code"))
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(530, 110, 91, 21))
        self.label_13.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(640, 450, 81, 31))
        self.label_14.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_14.setObjectName("label_14")
        self.cgst_tot = QtWidgets.QLineEdit(Form)
        self.cgst_tot.setEnabled(False)
        self.cgst_tot.setGeometry(QtCore.QRect(730, 450, 113, 27))
        self.cgst_tot.setStyleSheet("color: rgb(0, 0, 0);")
        self.cgst_tot.setReadOnly(True)
        self.cgst_tot.setObjectName("cgst_total")
        self.sgst_tot = QtWidgets.QLineEdit(Form)
        self.sgst_tot.setEnabled(False)
        self.sgst_tot.setGeometry(QtCore.QRect(730, 480, 113, 27))
        self.sgst_tot.setStyleSheet("color: rgb(0, 0, 0);")
        self.sgst_tot.setReadOnly(True)
        self.sgst_tot.setObjectName("sgst_total")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(640, 480, 81, 31))
        self.label_16.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_16.setObjectName("label_16")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(850, 480, 31, 21))
        self.label_15.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(850, 450, 31, 21))
        self.label_17.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(850, 420, 31, 21))
        self.label_18.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_18.setObjectName("label_18")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(640, 160, 171, 17))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(30, 220, 71, 17))
        self.label_19.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_19.setObjectName("label_19")
        try:
            self.completer = QtWidgets.QCompleter(self.all_past_invoice_ids)
        except Exception as e:
            self.completer = QtWidgets.QCompleter([])
        self.comboBox = QtWidgets.QLineEdit(Form)
        self.comboBox.setGeometry(QtCore.QRect(50, 470, 91, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setCompleter(self.completer)
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(570, 160, 51, 17))
        self.label_22.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_22.setObjectName("label_22")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(130, 220, 81, 17))
        self.label_20.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(230, 220, 81, 17))
        self.label_21.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_21.setObjectName("label_21")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(330, 220, 81, 17))
        self.label_23.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(440, 220, 81, 17))
        self.label_24.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(550, 220, 111, 17))
        self.label_25.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_25.setObjectName("label_25")
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setText("Alert")
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok) 

        self.pushButton_3.clicked.connect(self.get_values_from_user)
        self.pushButton.clicked.connect(self.get_values_from_table)
        self.pushButton_2.clicked.connect(self.reset_all)
        self.pushButton_4.clicked.connect(self.print_previous)
        self.client.returnPressed.connect(self.autofill_gst)
        self.gst.returnPressed.connect(self.autofill_client)
        self.part_no.returnPressed.connect(self.autofill_part_info)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Billing System"))
        self.label_10.setText(_translate("Form", "CHEMITECH INDUSTRIES"))
        self.label_7.setText(_translate("Form", "Total"))
        self.label_11.setText(_translate("Form", "EXPERT IN ALL TYPES OF ELECTRO PLATING"))
        self.label.setText(_translate("Form", "Part No."))
        self.label_12.setText(_translate("Form", "Search Past Invoice"))
        self.pushButton_4.setText(_translate("Form", "Print"))
        self.label_2.setText(_translate("Form", " Description"))
        self.pushButton.setText(_translate("Form", "Generate Bill"))
        self.pushButton_3.setText(_translate("Form", "Add Item"))
        self.label_3.setText(_translate("Form", " Qty"))
        self.label_9.setText(_translate("Form", "Rs"))
        self.label_4.setText(_translate("Form", "Rate"))
        self.label_6.setText(_translate("Form", "Client Name"))
        self.pushButton_2.setText(_translate("Form", "Reset"))
        self.label_8.setText(_translate("Form", "Grand Total"))
        self.label_13.setText(_translate("Form", "GSTIN No."))
        self.label_14.setText(_translate("Form", "CGST @ 9%"))
        self.label_16.setText(_translate("Form", "SGST @ 9%"))
        self.label_15.setText(_translate("Form", "Rs"))
        self.label_17.setText(_translate("Form", "Rs"))
        self.label_18.setText(_translate("Form", "Rs"))
        self.label_5.setText(_translate("Form", "Actual Plating Thickness"))
        self.label_19.setText(_translate("Form", "Specified"))
        self.label_22.setText(_translate("Form", "Lot No."))
        self.label_20.setText(_translate("Form", "Observed 1"))
        self.label_21.setText(_translate("Form", "Observed 2"))
        self.label_23.setText(_translate("Form", "Observed 3"))
        self.label_24.setText(_translate("Form", "Observed 4"))
        self.label_25.setText(_translate("Form", "HSN / SAC Code"))
        self.tot.setText(_translate("Form", "0", None))
        self.cgst_tot.setText(_translate("Form", "0", None))
        self.sgst_tot.setText(_translate("Form", "0", None))
        self.grand_tot.setText(_translate("Form", "0", None))


if __name__ == "__main__":
    import sys
    from datetime import date
    import webbrowser, os    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

