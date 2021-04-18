<template>
    <div class="container">
        <div class="list-group mb-5" v-for="link in links">
            <a :href="link.nro" class="list-group-item list-group-item-action flex-column align-items-start mt-3">
                <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">{{ link.titulo }}</h5>
                </div>
                <p class="mb-1">{{ link.texto }}</p>
            </a>
        </div>
    </div>
</template>


<script>
        export default {
            data() {
                return {
                    links: [
                        {
                            nro: "/python/estruturaSequencial/ex1",
                            texto: "1. Faça um Programa que mostre a mensagem 'Alo mundo' na tela.",
                            titulo: "Exercício 1"
                        }, 
                        {
                            nro: "/python/estruturaSequencial/ex2",
                            texto: "2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].",
                            titulo: "Exercício 2"
                        },
                        {
                            nro: "/python/estruturaSequencial/ex3",
                            texto: "3. Faça um Programa que peça dois números e imprima a soma.",
                            titulo: "Exercício 3"
                        },
                        {
                            nro: "/python/estruturaSequencial/ex4",
                            texto: "4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.",
                            titulo: "Exercício 4"
                        },
                        {
                            nro: "/python/estruturaSequencial/ex5",
                            texto: "5. Faça um Programa que converta metros para centímetros.",
                            titulo: "Exercício 5"
                        },
                        {
                            nro: "/python/estruturaSequencial/ex6",
                            texto: "6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.",
                            titulo: "Exercício 6"
                        },
                        {
                            nro: "/python/estruturaSequencial/ex7",
                            texto: "7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.",
                            titulo: "Exercício 7"
                        },
                        {
                            nro: "/python/estruturaSequencial/ex8",
                            texto: "8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.",
                            titulo: "Exercício 8"
                        },
                        {
                            nro: "/python/estruturaSequencial/ex9",
                            texto: "9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.C = 5 * ((F - 32) / 9).",
                            titulo: "Exercício 9"
                        },
                        {
                            nro: "/python/estruturaSequencial/ex10",
                            texto: "10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.",
                            titulo: "Exercício 10"
                        },
                        {
                            nro: "/python/estruturaSequencial/ex11",
                            texto: "11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: a) o produto do dobro do primeiro com metade do segundo. b) a soma do triplo do primeiro com o terceiro. c) o terceiro elevado ao cubo.",
                            titulo: "Exercício 11"
                        },
                        {
                            nro: "/python/estruturaSequencial/ex12",
                            texto: "12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58.",
                            titulo: "Exercício 12"
                        },
                        {
                            nro: "/python/estruturaSequencial/ex13",
                            texto: "13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: a) Para homens: (72.7*h) - 58 b) Para mulheres: (62.1*h) - 44.7",
                            titulo: "Exercício 13"
                        },
                        {
                            nro: "/python/estruturaSequencial/ex14",
                            texto: "14. João Papo - de - Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo(50 quilos) deve pagar uma multa de R$ 4, 00 por quilo excedente.João precisa que você faça um programa que leia a variável peso(peso de peixes) e calcule o excesso.Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.Imprima os dados do programa com as mensagens adequadas.",
                            titulo: "Exercício 14"
                        },
                        {
                            nro: "/python/estruturaSequencial/ex15",
                            texto: "15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: a) salário bruto. b) quanto pagou ao INSS. c) quanto pagou ao sindicato. d) o salário líquido. e) calcule os descontos e o salário líquido",
                            titulo: "Exercício 15"
                        },
                        //{ nro: "/python/estruturaSequencial/exemplo_para_form1entrada?nro=2&entradas=1", texto: "A. Exercicio de teste de funcionalidade." }
                    ]
                };
            }
        };
</script>