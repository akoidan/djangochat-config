static files for https://github.com/Deathangel908/djangochat


# SASS  questions
   Can I minify inputs here?
       select,
        textarea,
        div[contenteditable],
        input[type=text], input[type=password],input [type=email], input[type=date]
   How to move selector into mixing
        @mixin inputs()
            select,
            textarea,
            div[contenteditable],
            input[type=text], input[type=password],input [type=email], input[type=date]
   Is there a sass workouround withotu code duplicaiton to  deal with selector that contain invalid selector for firefox:
        button,
        input[type=file]::-webkit-file-upload-button {
          background:red;
        }
      this selector won't work even for button in firefox