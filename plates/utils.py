import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from io import BytesIO
import base64


def get_image():
    # create a byte buffer for the image to save
    buffer = BytesIO()
    # create the plot with the use of BytesIO object as it's 'file'
    plt.savefig(buffer, format='png')
    plt.close()
    # set the cursor to the beginning of the stream
    buffer.seek(0)
    # retrieve the entire content of the 'file'
    image_png = buffer.getvalue()

    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    # free the memory of the buffer
    buffer.close()

    return graph


def plate_error(df):
    return df[(df['predicted_color'] != df['gt_color']) | (df['predicted_emirate'] != df['gt_emirate']) | (
            df['predicted_number'] != df['gt_number']) | (df['predicted_code'] != df['gt_code'])]


def unpackGroups(x):
    return [x.index, x.values]


def generate_all_plates_count_by_time(plates_df):
    categories, values = unpackGroups(plates_df.groupby(['image_time']).size())
    hours = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
             '19', '20', '21', '22', '23', '24']
    vs = [0 for i in range(len(hours))]
    for c in categories:
        vs[list(categories).index(c)] = values[list(categories).index(c)]
    plt.title("All plates count by time")
    plt.bar(hours, vs)
    plt.xticks(rotation=45)
    plt.tight_layout()
    graph = get_image()
    return graph


def generate_all_plates_count_by_emirate_graph(df):
    all_emirates = df[["predicted_emirate", "gt_emirate"]].values.ravel()
    all_emirates = pd.unique(all_emirates)
    emirates_plates_count = df['gt_emirate'].value_counts().values
    plt.title("All plates count by emirate")
    plt.bar(all_emirates, emirates_plates_count)
    plt.xticks(rotation=45)
    plt.tight_layout()
    graph = get_image()
    return graph


def generate_all_plates_count_by_emirate_color(plates_df):
    emirates_colors = plates_df[['gt_emirate', 'gt_color']].agg('-'.join, axis=1)
    emirates_colors_count = emirates_colors.value_counts().values
    emirates_colors = pd.unique(emirates_colors)
    plt.title("All plates count by emirate-color")
    plt.bar(emirates_colors, emirates_colors_count)
    plt.xticks(rotation=45)
    plt.tight_layout()
    graph = get_image()
    return graph


def generate_all_plates_count_by_attributes_type(plates_df):
    attributes = ['Number', 'Color', 'Emirate', 'Code']
    counts = []
    for attribute in attributes:
        predicted_attribute = 'predicted_' + attribute.lower()
        gt_attribute = 'gt_' + attribute.lower()
        counts.append(plates_df[plates_df[gt_attribute] != ""].shape[0])
    title = 'All plates count by attributes type'
    plt.title(title)
    plt.bar(attributes, counts)
    plt.xticks(rotation=0)
    plt.tight_layout()
    graph = get_image()
    return graph


def generate_all_plates_error_count_by_emirate(plates_df):
    errors = plate_error(plates_df)
    categories, values = unpackGroups(errors.groupby(['gt_emirate']).size())
    x = [l.upper() for l in categories]
    title = 'All plates error count by emirate'
    plt.title(title)
    plt.bar(x, values)
    plt.xticks(rotation=45)
    plt.tight_layout()
    graph = get_image()
    return graph


def generate_all_plates_error_count_by_emirate_color(plates_df):
    errors = plate_error(plates_df)
    categories, values = unpackGroups(errors.groupby(['gt_emirate', 'gt_color']).size())
    emirates_colors = plates_df[['gt_emirate', 'gt_color']].agg('-'.join, axis=1)
    emirates_colors = pd.unique(emirates_colors)
    title = 'All plates error count by emirate-color'
    plt.title(title)
    plt.bar(emirates_colors, values)
    plt.xticks(rotation=45)
    plt.tight_layout()
    graph = get_image()
    return graph


def generate_all_plates_error_count_by_attribute_type(plates_df):
    attributes = ['Number', 'Color', 'Emirate', 'Code']
    counts = []
    for attribute in attributes:
        pred_attribute = 'predicted_' + attribute.lower()
        gt_attribute = 'gt_' + attribute.lower()
        counts.append(plates_df[plates_df[pred_attribute] != plates_df[gt_attribute]].shape[0])
    title = 'All plates error count by attribute-type'
    plt.title(title)
    plt.bar(attributes, counts)
    plt.xticks(rotation=45)
    plt.tight_layout()
    graph = get_image()
    return graph


def generate_all_plates_error_count_by_time(plates_df):
    errors = plate_error(plates_df)
    categories, values = unpackGroups(errors.groupby(['image_time']).size())
    hours = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
             '19', '20', '21', '22', '23', '24']
    vs = [0 for i in range(len(hours))]
    for c in categories:
        vs[list(categories).index(c)] = values[list(categories).index(c)]
    title = 'All plates error count by time'
    plt.title(title)
    plt.bar(hours, vs)
    plt.xticks(rotation=45)
    plt.tight_layout()
    graph = get_image()
    return graph


def generate_all_attributes_error_count_by_time(plates_df):
    errors = plate_error(plates_df)
    attributes = ['Number', 'Color', 'Emirate', 'Code']
    counts = []
    for attribute in attributes:
        pred_attribute = 'predicted_' + attribute.lower()
        gt_attribute = 'gt_' + attribute.lower()
        counts.append(plates_df[plates_df[pred_attribute] != plates_df[gt_attribute]].shape[0])

    sns.set_theme(style="whitegrid")
    sns.boxplot(x=attributes, y=counts, data=counts)
    graph = get_image()
    return graph
