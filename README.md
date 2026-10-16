# 複利計算アプリ

ローン返済、投資・積立の計算をブラウザで行う静的Webアプリ。

[公開サイト](https://tommy780103.github.io/Compound-Interest-Calculator/)

## 構成
- index.html：画面、スタイル、計算ロジック。
- icon.svg：青い背景に成長グラフを描いたアイコン原本。
- apple-touch-icon.png：iPhoneホーム画面向け180×180。不透明で、角丸処理はOSに任せる。
- favicon.png：48×48。icon-192.png、icon-512.png：その他のサイズ用。
- scripts/build-icons.py：ImageMagickを使用するPNG生成処理。

## ローカル表示
プロジェクト直下で実行し、表示されたアドレスをブラウザで開く。

```bash
python3 -m http.server 8000
```

## アイコンの再生成
ImageMagickが必要。

```bash
python3 scripts/build-icons.py
```

## iPhoneでの追加
Safariで公開サイトを開き、共有メニューから「ホーム画面に追加」を選ぶ。追加画面でグラフのアイコンを確認する。古いアイコンが残る場合は、新しく追加して動作を確認してから古い項目を取り除く。アイコン追加による計算処理や保存仕様の変更はない。

## 確認
HTMLの相対パス、PNGの寸法・不透明性、公開後のHTMLと画像取得を確認する。iPhone実機での追加表示は別途確認が必要。
