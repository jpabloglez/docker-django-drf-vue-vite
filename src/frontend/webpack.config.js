/* Configure webpack 

Reference: https://lmiller1990.github.io/electic/posts/20200406_webpack_for_vue_3.html

*/

const path = require('path');

const { VueLoaderPlugin } = require('vue-loader');

module.exports = {
  entry: './src/main.ts',
  output: {
    path: path.resolve(__dirname, './dist'),
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      }
    ],
    plugins: [
        new VueLoaderPlugin()
    ]
  }
}