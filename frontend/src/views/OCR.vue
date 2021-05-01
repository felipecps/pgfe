<template>
    <div class="container">
        <div>
            <v-file-input accept="image/png, image/jpeg, image/bmp"
                          placeholder="Imagem"
                          show-size
                          counter
                          label="Selecione uma imagem para extração de texto"
                          v-model="imageData"
                          prepend-icon="mdi-camera"></v-file-input>
            <v-btn @click="ocr">Extrair texto</v-btn>
        </div>
        <div class="mt-3">
            <b-alert v-if="mostra_ocr" show>{{ resp.ocr }}</b-alert>
        </div>
    </div>
</template>




<script>
    import axios from 'axios';
    var mylib = require('@/modulos/OCR/ocr.js');

    import Tesseract from 'tesseract.js';

    export default {
        data() {
            return {
                imageData: [],
                files: [],
                resp: {
                    ocr: "",
                    status: 0
                }, 
                mostra_ocr: false
            }
        },
        methods: {
            onUpload() {
                mylib.ocr()              
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
                            this.resp.ocr = res.data.resposta
                            console.log("Success!");
                            //console.log({ response });
                        })
                        .catch(error => {
                            console.log({ error });
                        });
                } else {
                    console.log("there are no files.");
                }
            },
            ocr() {
                Tesseract.recognize(
                    'http://127.0.0.1:8887/eng_bw.png',
                    'eng',
                    { logger: m => console.log(m) }
                ).then(({ data: { text } }) => {
                    console.log(text);
                })
            }
        }
            
    };
</script>
