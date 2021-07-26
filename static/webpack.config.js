const path = require('path');
const mode = process.env.NODE_ENV || 'development';
const Dotenv = require('dotenv-webpack');
const {
  CleanWebpackPlugin
} = require('clean-webpack-plugin');


module.exports = env => {
  return {
    mode: "development",
    devtool: 'cheap-module-source-map',
    entry: {
      index: path.join(__dirname, 'src', 'index.tsx'),
    },
    output: {
      filename: 'dist/[name].js',
      path: path.resolve(__dirname, 'dist'),
    },
    resolve: {
      extensions: ['.ts', '.tsx', '.js', '.jsx'],
    },
    devServer: {
      port: 3000,
      hot: true,
      overlay: true,
      disableHostCheck: true,
    },
    plugins: [
      new Dotenv(),
      new CleanWebpackPlugin(),
    ],
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
          },
        },

      ],
    },
  }
};