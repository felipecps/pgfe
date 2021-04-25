<template>
    <div class="container">
 
        <v-file-input accept="image/png, image/jpeg, image/bmp"
                      placeholder="Pick an avatar"
                      show-size 
                      counter 
                      chips 
                      label="Arquivo Geral"
                      v-model="imageData"
                      prepend-icon="mdi-camera"></v-file-input>
        <v-btn @click="onUpload">Upload</v-btn>

    </div>
</template>




<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                imageData: [],
                files: []
            }
        },
        methods: {
            onUpload() {
                console.log("upload")
                let formData = new FormData();
                formData.append('file', this.imageData);
                axios.post(
                    "http://localhost:5000/ocr"
                    , formData
                    , { headers: { "Content-Type": "multipart/form-data" } }
                )
                    .then(response => {
                        //...
                    })
                    .catch(e => {
                        //...
                    })                
            },
            submitFiles() {
                if (this.files) {
                    let formData = new FormData();

                    // files
                    for (let file of this.files) {
                        formData.append("files", file, file.name);
                    }

                    // additional data
                    formData.append("test", "foo bar");

                    axios
                        .post("http://localhost:5000/ocr", formData)
                        .then(response => {
                            console.log("Success!");
                            console.log({ response });
                        })
                        .catch(error => {
                            console.log({ error });
                        });
                } else {
                    console.log("there are no files.");
                }
            }
        }
            
    };
</script>
