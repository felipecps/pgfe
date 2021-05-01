<template>
    <div class="container">
        <div>
            <v-file-input accept="image/png, image/jpeg, image/bmp"
                          placeholder="Imagem"
                          show-size
                          counter
                          label="Selecione uma imagem para extração de texto"
                          v-model="files"
                          prepend-icon="mdi-camera"></v-file-input>
            <v-btn @click="ocr">Extrair texto</v-btn>
        </div>
        <div class="mt-3">
            <b-alert v-if="mostra_ocr" show>{{ texto_ocr }}</b-alert>
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
                files: [],
                resp: {
                    ocr: "",
                    status: 0
                }, 
                mostra_ocr: false,
                texto_ocr: ""

            }
        },
        methods: {
            onUpload() {
                mylib.ocr()              
            },
            /*submitFiles() {
            -                if (this.files) {
            -                    let formData = new FormData();
            -
            -                    // files
            -                    for (let file of this.files) {
            -                        formData.append("files", file, file.name);
            -                    }
            -
            -                    // additional data
            -                    formData.append("test", "foo bar");
            -
            -                    axios
            -                        .post("http://localhost:5000/ocr", formData)
            -                        .then(response => {
            -                            this.resp.ocr = res.data.resposta
            -                            console.log("Success!");
            -                            //console.log({ response });
            -                        })
            -                        .catch(error => {
            -                            console.log({ error });
            -                        });
            -                } else {
            -                    console.log("there are no files.");
            -                }
            -            },*/
            ocr() {
                console.log(this.files)
                Tesseract.recognize(
                    this.files,
                    'eng',
                    { logger: m => console.log(m) }
                ).then(({ data: { text } }) => {
                    this.mostra_ocr = true
                    this.texto_ocr = text
                })
            }
        }
    };
</script>
