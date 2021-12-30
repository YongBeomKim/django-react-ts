const path = require('path');
const mode = process.env.NODE_ENV || 'development';
const Dotenv = require('dotenv-webpack');
const ErrorOverlayPlugin = require('error-overlay-webpack-plugin')
const {
  CleanWebpackPlugin
} = require('clean-webpack-plugin');


module.exports = env => {
  return {
    mode: "development",
    entry: {
      index: path.join(__dirname, 'src', 'index.tsx'),
    },
    output: {
      filename: '[name].js',
      path: path.resolve(__dirname, 'dist'),
    },
    plugins: [
      new Dotenv(),
      new CleanWebpackPlugin(),
      new ErrorOverlayPlugin(),
    ],
    // devtool: 'cheap-module-source-map',
    resolve: {
      extensions: ['.ts', '.tsx', '.js', '.jsx'],
    },
    devServer: {
      port: 3000,
      hot: true,
      overlay: {
        errors: true,
        warnings: true
      },
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
        "Access-Control-Allow-Headers": "X-Requested-With, content-type, Authorization"
      }
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