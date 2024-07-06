# GoogleSearchSuggestChecker
Google検索サジェストチェックアプリ

## 目次
- [プロジェクト概要](#プロジェクト概要)
- [特徴](#特徴)
- [技術スタック](#技術スタック)
- [アプリの使用方法](#アプリの使用方法)
  - [Streamlit Cloudを使用する](#streamlit-cloudを使用する)
  - [Google Colabとngrokを使用する](#google-colabとngrokを使用する)
- [セットアップ](#セットアップ)
  - [前提条件](#前提条件)
  - [インストール手順](#インストール手順)
- [注意](#注意)
- [コントリビューション](#コントリビューション)

## プロジェクト概要
このプロジェクトは、指定されたクエリに対するGoogleの検索サジェスト結果を取得し表示するWebアプリです。Streamlitを利用して構築され、Streamlit Cloudを通じて公開されます。

## 特徴
- 指定された検索クエリに対するGoogle検索サジェスト結果の取得。
- サジェスト結果の直感的な表示。
- ユーザーが入力したクエリに基づいてリアルタイムで結果を表示。

## 技術スタック
- Streamlit
- Requests
- Google Suggest API

## アプリの使用方法
### Streamlit Cloudを使用する
Streamlit Cloudでホストされているため、特別な実行手順は不要です。以下のURLからアクセスできます。
[GoogleSearchSuggestChecker](https://appsearchsuggestchecker-8cgj6vcqovha8vrfpzxd5h.streamlit.app/)

### Google Colabとngrokを使用する
Google Colabとngrokを使用してアプリを実行する方法については、セットアップ手順を参照してください。

## セットアップ
### 前提条件
- Python 3.8 以上がインストールされていること。
- ngrokのアカウントを持っていること（Google Colabとngrokを使用する場合）。

### インストール手順
1. リポジトリをクローンします。
    ```bash
    git clone このリポジトリのURL
    cd このリポジトリのディレクトリ
    ```
2. 必要なPythonパッケージをインストールします。
    ```bash
    pip install -r requirements.txt
    ```
    
## 注意
このアプリは公開的なデモ用途に最適化されています。

## コントリビューション
プロジェクトへのコントリビューションに興味がある方は、Pull RequestやIssueを通じてご提案ください。
