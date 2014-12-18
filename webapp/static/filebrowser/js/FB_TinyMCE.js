var FileBrowserDialogue = {
    fileSubmit : function (FileURL) {
        window.parent.document.getElementById(window.parent.popup_window_input).value = FileURL;
        window.parent.active_editor.activeEditor.windowManager.close();
    }
}