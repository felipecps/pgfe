<template>
    <div class="container">
        <v-file-input accept="image/*"
                      label="File input"></v-file-input>

        <hr />

        <v-file-input accept="image/png, image/jpeg, image/bmp"
                      placeholder="Pick an avatar"
                      v-model="imageData"
                      prepend-icon="mdi-camera"></v-file-input>
        <v-btn color="primary" @click="onUpload">Upload</v-btn>






        <v-layout>
            <v-flex>
                <v-file-input show-size counter chips multiple label="Arquivo Geral" ref="myfile" v-model="files"></v-file-input>
            </v-flex>
            <v-flex>
                <v-btn color="primary" text @click="submitFiles">test</v-btn>
            </v-flex>
        </v-layout>




    </div>
</template>




<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                imageData: '',
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
        },
        mounted: {

        },
        computed: {
            //https://guivern.hashnode.dev/vue-js-differences-between-computed-and-watch
        },
        watch: {

        }
            
    };
</script>
