<template>
    <div class="container">
        <b-card border-variant="light" header="Estrutura Sequencial" align="left">
            <div v-for="link in links">
                <b-link :href="link.nro">{{ link.texto }}</b-link>
            </div>
        </b-card>        
    </div>
</template>


<script>
        export default {
            data() {
                return {
                    links: [
                        { nro: "/python/estruturaSequencial/ex1", texto: "1. Faça um Programa que mostre a mensagem 'Alo mundo' na tela." }, 
                        { nro: "/python/estruturaSequencial/ex2", texto: "2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]." },
                        { nro: "/python/estruturaSequencial/ex3", texto: "3. Faça um Programa que peça dois números e imprima a soma." },
                        { nro: "/python/estruturaSequencial/ex4", texto: "4. Faça um Programa que peça as 4 notas bimestrais e mostre a média." },
                        { nro: "/python/estruturaSequencial/ex5", texto: "5. Faça um Programa que converta metros para centímetros." },
                        { nro: "/python/estruturaSequencial/ex6", texto: "6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área." },
                        { nro: "/python/estruturaSequencial/ex7", texto: "7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário." },
                        { nro: "/python/estruturaSequencial/ex8", texto: "8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês." },
                        { nro: "/python/estruturaSequencial/ex9", texto: "9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.C = 5 * ((F - 32) / 9)." },
                        { nro: "/python/estruturaSequencial/ex10", texto: "10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit." },
                        {
                            nro: "/python/estruturaSequencial/ex11",
                            texto: "11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: a) o produto do dobro do primeiro com metade do segundo. b) a soma do triplo do primeiro com o terceiro. c) o terceiro elevado ao cubo."
                        },
                        {
                            nro: "/python/estruturaSequencial/ex12",
                            texto: "12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58."
                        },
                        {
                            nro: "/python/estruturaSequencial/ex13",
                            texto: "13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: a) Para homens: (72.7*h) - 58 b) Para mulheres: (62.1*h) - 44.7"
                        },
                        //{ nro: "/python/estruturaSequencial/exemplo_para_form1entrada?nro=2&entradas=1", texto: "A. Exercicio de teste de funcionalidade." }
                    ]
                };
            }
        };
</script>