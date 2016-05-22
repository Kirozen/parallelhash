""" phash_ui.py """

__author__ = "Etienne Faisant"
__date__ = "2015-03-11"

import wx
import uibase
import phash
import os
from phash import BaseCounter, format_size


class GuiCounter(BaseCounter):

    def __init__(self, total=0, total_files=0, initval=0, initfval=0):
        BaseCounter.__init__(self, total, total_files, initval, initfval)

    def show_increment(self):
        print("Progression :", self.fval.value, "/", self.total_files, "files ", format_size(self.val.value),
              "/", format_size(self.total), "%.2f%%" % (self.val.value / self.total * 100.0), " " * 10, end="\r")

    def show_increment_count(self):
        print("Progression :", self.val.value, "/", self.total, "files %.2f%%" %
              (self.val.value / self.total * 100.0), " " * 10, end="\r")


class ParallelHashFrame(uibase.BaseFrame):

    def __init__(self, parent=None):
        uibase.BaseFrame.__init__(self, parent)

    # Handlers for BaseFrame events.
    def signal_findhashfile(self, event):
        openFileDialog = wx.FileDialog(
            self, "Open Parallel Hash file", "", "", "PLH file (*.plh)|*.plh", wx.FD_OPEN)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        self.m_textCtrl_hashfile.SetLabelText(openFileDialog.GetPath())

    def enable_components(self, enable=True):
        self.m_textCtrl_folder.Enable(enable)
        self.m_button_addfolder.Enable(enable)
        self.m_button_addfile.Enable(enable)

        self.m_radio_md5.Enable(enable)
        self.m_radio_sha1.Enable(enable)
        self.m_radio_sha256.Enable(enable)
        self.m_radio_sha512.Enable(enable)

    def signal_btn_hash(self, event):
        self.enable_components()

    def signal_btn_verify(self, event):
        self.enable_components(False)

    def signal_btn_compare(self, event):
        self.enable_components()

    def signal_addfile(self, event):
        openFileDialog = wx.FileDialog(
            self, "Add files", "", "", "(*.*)|*.*", wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        self.m_textCtrl_folder.AppendText(openFileDialog.GetPath() + ", ")

    def signal_addfolder(self, event):
        openFileDialog = wx.DirDialog(
            self, "Add folder", "", wx.DD_DIR_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        self.m_textCtrl_folder.AppendText(openFileDialog.GetPath() + ", ")

    def signal_go(self, event):
        paths = self.m_textCtrl_folder.GetValue().split(', ')
        files_list, total_size = self.build_list(paths)
        files_list.sort()
        nfiles = len(files_list)

    def build_list(self, paths):
        files_list = []
        total_size = 0
        for path in paths:
            for root, _, files in os.walk(path):
                self.m_staticText_status.SetLabelText("Status: %d files discovered - %s" %
                                                      (len(files_list), format_size(total_size)))
                for file in files:
                    total_size += os.path.getsize(os.path.join(root, file))
                    files_list.append(os.path.join(root, file))
        self.m_staticText_status.SetLabelText("Status: %d files discovered - %s" %
                                              (len(files_list), format_size(total_size)))
        return files_list, total_size


class MyApp(wx.App):

    def OnInit(self):
        frame = ParallelHashFrame()
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp(redirect=False)
    app.MainLoop()
