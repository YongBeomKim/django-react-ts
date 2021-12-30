const path = require('path');
const mode = process.env.NODE_ENV || 'development';
const Dotenv = require('dotenv-webpack');
const ErrorOverlayPlugin = require('error-overlay-webpack-plugin')
const {
  CleanWebpackPlugin
} = require('clean-webpack-plugin');


module.exports = env => {
  return {
    mode: 'production',
    devtool: 'hidden-source-map', 
    entry: {
      index: path.join(__dirname, 'src', 'index.tsx'),
    },
    output: {
      filename: '[name].js',
      path: path.resolve(__dirname, 'dist'),
      publicPath: '/dist/',
    },
    plugins: [
      new Dotenv(),
      new CleanWebpackPlugin(),
      new ErrorOverlayPlugin(),
    ],
    resolve: {
      extensions: ['.ts', '.tsx', '.js', '.jsx'],
    },
    module: {
      rules: [
        {
          test: /\.(js|jsx|ts|tsx)$/,
          loader: require.resolve("babel-loader"),
          exclude: /node_modules/,
          options: {
            presets: [
              require.resolve("@babel/preset-react"),
              require.resolve("@babel/preset-typescript"),
            ],
            plugins: [
              "@babel/plugin-proposal-class-properties",
              "@babel/plugin-transform-runtime"
            ],
          },
        },

        {
          test: [/\.css$/, /\.s[ac]ss$/i],
          use: ['style-loader', 'css-loader', 'sass-loader'],
        },
        
      ],
    },
  }
};