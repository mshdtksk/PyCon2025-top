import streamlit as st
from datetime import datetime
import pandas as pd

# ページ設定
st.set_page_config(
    page_title="最適化アプリケーション ポータル",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# カスタムCSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1e3d59;
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    
    .app-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
        border-left: 4px solid #667eea;
    }
    
    .app-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.2);
    }
    
    .app-title {
        font-size: 1.3rem;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    
    .app-description {
        color: #5a6c7d;
        margin-bottom: 1rem;
        line-height: 1.6;
    }
    
    .app-link {
        display: inline-block;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 1rem;
    }
    
    .category-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #34495e;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #667eea;
    }
    
    .stats-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        padding: 1.5rem;
        color: white;
        margin-bottom: 2rem;
    }
    
    .stat-item {
        text-align: center;
        padding: 1rem;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    </style>
    """, unsafe_allow_html=True)

# アプリケーションデータ
apps_data = [
    {
        "title": "ネットワーク設計業務の数理モデル",
        "category": "ネットワーク最適化",
        "description": "連結巡回路による頂点被覆問題の数理モデルを用いたネットワーク設計の最適化ツール。実務への適用を考慮した設計支援システム。",
        "url": "https://st-app-nw-circle4-504242909255.asia-northeast1.run.app/",
        "tags": ["ネットワーク", "グラフ理論", "最適化"],
        "icon": "🌐"
    },
    {
        "title": "工事立合者手配最適化アプリ",
        "category": "リソース配置",
        "description": "集合被覆問題（Set Cover Problem）を応用した工事立合者の効率的な手配を実現する最適化アプリケーション。",
        "url": "https://st-app-setcoverproblem2-504242909255.asia-northeast1.run.app/",
        "tags": ["スケジューリング", "リソース管理", "集合被覆"],
        "icon": "👷"
    },
    {
        "title": "巡回セールスマン問題（TSP）",
        "category": "経路最適化",
        "description": "古典的な最適化問題であるTSPを解くアプリケーション。効率的な巡回経路の探索と可視化機能を提供。",
        "url": "https://streamlit20250322tsp-h9bxa0dkdqgwfqgx.eastasia-01.azurewebsites.net/",
        "tags": ["TSP", "経路探索", "組合せ最適化"],
        "icon": "🗺️"
    },
    {
        "title": "万博訪問ルート最適化アプリ",
        "category": "経路最適化",
        "description": "万博会場内の効率的な訪問ルートを計算する最適化アプリ。待ち時間や移動距離を考慮した最適なルート提案。",
        "url": "https://st-app-expo-504242909255.asia-northeast1.run.app/",
        "tags": ["イベント", "ルート最適化", "観光"],
        "icon": "🎪"
    }
]

# ヘッダー
st.markdown('<h1 class="main-header">🚀 最適化アプリケーション ポータル</h1>', unsafe_allow_html=True)

# サイドバー
with st.sidebar:
    st.markdown("### 📊 フィルター")
    
    # カテゴリフィルター
    categories = list(set([app["category"] for app in apps_data]))
    selected_categories = st.multiselect(
        "カテゴリを選択",
        options=categories,
        default=categories
    )
    
    # タグフィルター
    all_tags = []
    for app in apps_data:
        all_tags.extend(app["tags"])
    unique_tags = list(set(all_tags))
    
    selected_tags = st.multiselect(
        "タグを選択",
        options=unique_tags,
        default=[]
    )
    
    st.markdown("---")
    
    # 情報セクション
    st.markdown("### ℹ️ ポータル情報")
    st.info(f"登録アプリ数: {len(apps_data)}")
    st.info(f"カテゴリ数: {len(categories)}")
    st.info(f"最終更新: {datetime.now().strftime('%Y-%m-%d')}")

# メインコンテンツ
# 統計情報
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("総アプリ数", len(apps_data), "📱")
with col2:
    st.metric("カテゴリ数", len(categories), "📁")
with col3:
    st.metric("総タグ数", len(unique_tags), "🏷️")
with col4:
    st.metric("アクティブ", "100%", "✅")

st.markdown("---")

# タブで表示形式を選択
tab1, tab2, tab3 = st.tabs(["🎯 カード表示", "📋 リスト表示", "📊 カテゴリ別表示"])

# フィルタリング処理
filtered_apps = apps_data
if selected_categories:
    filtered_apps = [app for app in filtered_apps if app["category"] in selected_categories]
if selected_tags:
    filtered_apps = [app for app in filtered_apps if any(tag in selected_tags for tag in app["tags"])]

with tab1:
    # カード表示
    if filtered_apps:
        cols = st.columns(2)
        for idx, app in enumerate(filtered_apps):
            with cols[idx % 2]:
                st.markdown(f"""
                    <div class="app-card">
                        <div class="app-title">{app['icon']} {app['title']}</div>
                        <div class="app-description">{app['description']}</div>
                        <div style="margin: 0.5rem 0;">
                            <span style="background: #f0f0f0; padding: 0.3rem 0.6rem; border-radius: 15px; font-size: 0.85rem; margin-right: 0.5rem;">
                                {app['category']}
                            </span>
                        </div>
                        <div style="margin: 0.5rem 0;">
                            {' '.join([f'<span style="background: #e8f4f8; color: #667eea; padding: 0.2rem 0.5rem; border-radius: 10px; font-size: 0.8rem; margin-right: 0.3rem;">#{tag}</span>' for tag in app['tags']])}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                if st.button(f"アプリを開く", key=f"btn_{idx}"):
                    st.markdown(f'<meta http-equiv="refresh" content="0; url={app["url"]}">', unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.warning("選択した条件に一致するアプリケーションがありません。")

with tab2:
    # リスト表示
    if filtered_apps:
        df_data = []
        for app in filtered_apps:
            df_data.append({
                "アプリ名": f"{app['icon']} {app['title']}",
                "カテゴリ": app['category'],
                "説明": app['description'][:50] + "...",
                "タグ": ", ".join(app['tags']),
                "URL": app['url']
            })
        
        df = pd.DataFrame(df_data)
        
        # データフレームの表示
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "URL": st.column_config.LinkColumn("リンク")
            }
        )
    else:
        st.warning("選択した条件に一致するアプリケーションがありません。")

with tab3:
    # カテゴリ別表示
    if filtered_apps:
        for category in categories:
            category_apps = [app for app in filtered_apps if app["category"] == category]
            if category_apps:
                st.markdown(f'<div class="category-header">📂 {category}</div>', unsafe_allow_html=True)
                
                for app in category_apps:
                    with st.expander(f"{app['icon']} {app['title']}", expanded=False):
                        st.markdown(f"**説明:** {app['description']}")
                        st.markdown(f"**タグ:** {', '.join(app['tags'])}")
                        st.markdown(f"**URL:** {app['url']}")
                        
                        col1, col2 = st.columns([1, 4])
                        with col1:
                            if st.button("開く", key=f"cat_btn_{app['title']}"):
                                st.markdown(f'<meta http-equiv="refresh" content="0; url={app["url"]}">', 
                                          unsafe_allow_html=True)
    else:
        st.warning("選択した条件に一致するアプリケーションがありません。")

# フッター
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #7f8c8d; padding: 2rem 0;">
        <p>🚀 最適化アプリケーション ポータル</p>
        <p style="font-size: 0.9rem;">各種最適化問題を解決するアプリケーションを集約</p>
    </div>
    """, unsafe_allow_html=True)
