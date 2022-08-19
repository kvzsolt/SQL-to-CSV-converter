import data_handler
import wx
from ObjectListView import ObjectListView, ColumnDefn
from converter import converter

tables = [dict['Tables_in_{dbname}'.format(dbname=os.environ.get('MYSQL_DB_NAME'))] for dict in data_handler.get_database_name()]
toConvert = []


class Results(object):

    def __init__(self, name):
        self.name = name


class ProvPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        data = [Results(name) for name in tables]

        self.data = data

        self.resultsOlv = ObjectListView(self, style=wx.LC_REPORT | wx.SUNKEN_BORDER)

        self.setResults()

        convertBtn = wx.Button(self, label='Convert')
        convertBtn.Bind(wx.EVT_BUTTON, self.onConvert)

        mainSizer.Add(self.resultsOlv, 1, wx.EXPAND|wx.ALL, 1)
        mainSizer.Add(convertBtn, 0, wx.CENTER|wx.ALL, 5)
        self.SetSizer(mainSizer)

    def setResults(self):
        self.resultsOlv.SetColumns([
            ColumnDefn('Table Name', "left", 140,"name")
        ])
        self.resultsOlv.CreateCheckStateColumn()
        self.resultsOlv.SetObjects(self.data)

    def onConvert(self, event):
        objects = self.resultsOlv.GetObjects()
        for object, table in zip(objects, tables):
            if self.resultsOlv.IsChecked(object):
                toConvert.append(table)
        converter(toConvert)



class ProvFrame(wx.Frame):

    def __init__(self):
        title = 'SQL to CSV Converter by kvzsolt'
        wx.Frame.__init__(self, parent=None, title=title, size=(250, 250))
        ProvPanel(self)


if __name__ == "__main__":
    app = wx.App(False)
    frame = ProvFrame()
    frame.Show()
    app.MainLoop()

