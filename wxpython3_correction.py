""" wxpython3_correction.py """

__author__ = "Etienne Faisant"
__date__ = "2015-02-26"

import os
import os.path
import inspect
import sys

CORRECTIONS = [
    ["SetSizeHintsSz", "SetSizeHints"],
    ["AppendItem", "Append"],
    ["BlitPointSize", "Blit"],
    ["CalcBoundingBoxPoint", "CalcBoundingBox"],
    ["CrossHairPoint", "CrossHair"],
    ["DrawArcPoint", "DrawArc"],
    ["DrawBitmapPoint", "DrawBitmap"],
    ["DrawCheckMarkRect", "DrawCheckMark"],
    ["DrawCirclePoint", "DrawCircle"],
    ["DrawEllipsePointSize", "DrawEllipse"],
    ["DrawEllipseRect", "DrawEllipse"],
    ["DrawEllipticArcPointSize", "DrawEllipticArc"],
    ["DrawIconPoint", "DrawIcon"],
    ["DrawLinePoint", "DrawLine"],
    ["DrawPointPoint", "DrawPoint"],
    ["DrawRectanglePointSize", "DrawRectangle"],
    ["DrawRectangleRect", "DrawRectangle"],
    ["DrawRotatedTextPoint", "DrawRotatedText"],
    ["DrawRoundedRectanglePointSize", "DrawRoundedRectangle"],
    ["DrawRoundedRectangleRect", "DrawRoundedRectangle"],
    ["DrawTextPoint", "DrawText"],
    ["EndDrawing", "REMOVED"],
    ["FloodFillPoint", "FloodFill"],
    ["GetDeviceOriginTuple", "GetDeviceOrigin"],
    ["GetImpl", "REMOVED"],
    ["GetLogicalOriginTuple", "GetLogicalOrigin"],
    ["GetMultiLineTextExtent", "GetFullMultiLineTextExtent"],
    ["GetOptimization", "REMOVED"],
    ["GetPixelPoint", "GetPixel"],
    ["GetResolution", "GetPPI"],
    ["GetSizeMMTuple", "GetSizeMM"],
    ["Ok", "IsOk"],
    ["SetClippingRect", "SetClippingRegion"],
    ["SetClippingRegionAsRegion", "SetClippingRegion"],
    ["SetClippingRegionPointSize", "SetClippingRegion"],
    ["SetDeviceOriginPoint", "SetDeviceOrigin"],
    ["SetLogicalOriginPoint", "SetLogicalOrigin"],
    ["SetOptimization", "REMOVED"],
    ["StretchBlitPointSize", "StretchBlit"],
    ["ClientToScreenXY", "ClientToScreen"],
    ["ConvertDialogPointToPixels", "ConvertDialogToPixels"],
    ["ConvertDialogSizeToPixels", "ConvertDialogToPixels"],
    ["GetAdjustedBestSize", "GetEffectiveMinSize"],
    ["GetBestFittingSize", "GetEffectiveMinSize"],
    ["GetBestSizeTuple", "GetBestSize"],
    ["GetClientSizeTuple", "GetClientSize"],
    ["GetScreenPositionTuple", "GetScreenPosition"],
    ["GetSizeTuple", "GetSize"],
    ["GetToolTipString", "GetToolTipText"],
    ["HitTestXY", "HitTest"],
    ["IsExposedPoint", "IsExposed"],
    ["IsExposedRect", "IsExposed"],
    ["MakeModal", "REMOVED"],
    ["PopupMenuXY", "PopupMenu"],
    ["ScreenToClientXY", "ScreenToClient"],
    ["SetBestFittingSize", "SetInitialSize"],
    ["SetClientSizeWH", "SetClientSize"],
    ["SetDimensions", "SetSize"],
    ["SetHelpTextForId", "SetHelpText"],
    ["SetSizeHintsSz", "SetSizeHints"],
    ["SetToolTipString", "SetToolTip"],
    ["AddF", "Add"],
    ["AddItem", "Add"],
    ["AddSizer", "Add"],
    ["AddWindow", "Add"],
    ["DeleteWindows", "Clear"],
    ["GetItemIndex", "GetItem"],
    ["GetMinSizeTuple", "GetMinSize"],
    ["GetPositionTuple", "GetPosition"],
    ["InsertF", "Insert"],
    ["InsertItem", "Insert"],
    ["InsertSizer", "Insert"],
    ["InsertWindow", "Insert"],
    ["PrependF", "Prepend"],
    ["PrependItem", "Prepend"],
    ["PrependSizer", "Prepend"],
    ["PrependWindow", "Prepend"],
    ["RemovePos", "Remove"],
    ["RemoveSizer", "Remove"],
    ["RemoveWindow", "Remove"],
    ["wx.ST_SIZEGRIP", "wx.STB_SIZEGRIP"],
    ["u\"", "\""],
    ["import wx.aui", "import wx.lib.agw.aui as aui"],
    ["wx.aui.", "aui."],
    ["\t", " " * 4],
    ["( ", "("],
    [" )", ")"],
]


def getlist(path):
    allfiles = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(".py"):
                allfiles.append(os.path.join(root, f))
    return allfiles
    # current = inspect.getfile(inspect.currentframe())
    # return [f for f in allfiles if f != current and os.path.isfile(f)]


def correct(fname):
    lines = []
    print("Apply corrections on %s..." % (fname), end='')
    modifications = 0
    with open(fname) as reader:
        for line in reader:
            for correction in CORRECTIONS:
                index = line.find(correction[0])
                if index != -1:
                    line = line.replace(correction[0], correction[1])
                    modifications += 1
            if line.isspace():
                line = '\n'
            lines.append(line)
    if modifications:
        with open(fname, "w") as writer:
            writer.writelines(lines)
    print("OK (%d modifications)" % (modifications))


def workondir(path):
    print("Work on", path)
    files = getlist(path)
    for f in files:
        if not f.endswith(os.path.basename(__file__)):
            correct(f)

if __name__ == '__main__':
    print(os.path.basename(__file__))
    if len(sys.argv) == 2:
        workondir(sys.argv[1])
    else:
        workondir('sources')
