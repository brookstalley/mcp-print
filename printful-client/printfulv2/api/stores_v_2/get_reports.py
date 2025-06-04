import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_reports_report_types import GetReportsReportTypes
from ...models.get_reports_response_200 import GetReportsResponse200
from ...models.get_reports_response_400 import GetReportsResponse400
from ...models.get_reports_response_401 import GetReportsResponse401
from ...models.get_reports_response_404 import GetReportsResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    store_id: int,
    *,
    date_from: datetime.date,
    date_to: datetime.date,
    currency: Union[Unset, str] = UNSET,
    report_types: GetReportsReportTypes,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date_from = date_from.isoformat()
    params["date_from"] = json_date_from

    json_date_to = date_to.isoformat()
    params["date_to"] = json_date_to

    params["currency"] = currency

    json_report_types = report_types.value
    params["report_types"] = json_report_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/stores/{store_id}/statistics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetReportsResponse200, GetReportsResponse400, GetReportsResponse401, GetReportsResponse404]]:
    if response.status_code == 200:
        response_200 = GetReportsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GetReportsResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = GetReportsResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = GetReportsResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetReportsResponse200, GetReportsResponse400, GetReportsResponse401, GetReportsResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    store_id: int,
    *,
    client: AuthenticatedClient,
    date_from: datetime.date,
    date_to: datetime.date,
    currency: Union[Unset, str] = UNSET,
    report_types: GetReportsReportTypes,
) -> Response[Union[GetReportsResponse200, GetReportsResponse400, GetReportsResponse401, GetReportsResponse404]]:
    """Retrieve statistics for a single store

     Returns statistics for specified report types.

    You need to specify the report types you want to retrieve in the `report_types` query parameter as a
    comma-separated list,
    e.g. `report_types=sales_and_costs,profit`.

    **Note**: You cannot get statistics for a period longer than 6 months.

    #### Example

    To get statistics in the default currency of a store for `sales_and_costs` and `profit` reports for
    August 2022, you can use the
    following
    URL: https://api.printful.com/v2/stores/{id}/statistics?report_types=sales_and_costs,profit&date_fro
    m=2022-08-01&date_to=2022-08-31.

    ### Report types

    Currently, the following report types are available:

    | Report type                | Description                                              |
    |----------------------------|----------------------------------------------------------|
    | `sales_and_costs`          | Detailed information on sales and costs grouped by date. |
    | `sales_and_costs_summary`  | Short information on sales and costs grouped by date.    |
    | `printful_costs`           | Amount paid to Printful for fulfillment and shipping.    |
    | `profit`                   | Profit in the specified period.                          |
    | `total_paid_orders`        | The number of paid orders in the specified period.       |
    | `costs_by_amount`          | Information on costs by amount grouped by date.          |
    | `costs_by_product`         | Information on costs grouped by product.                 |
    | `costs_by_variant`         | Information on costs grouped by variant.                 |
    | `average_fulfillment_time` | Average time it took Printful to fulfill your orders.    |

    The response structure for the specific reports is documented in the response schema
    (`result.store_statistics.[reportName]`).

    Args:
        store_id (int):
        date_from (datetime.date):  Example: 2022-08-01.
        date_to (datetime.date):  Example: 2022-08-31.
        currency (Union[Unset, str]):  Example: USD.
        report_types (GetReportsReportTypes):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetReportsResponse200, GetReportsResponse400, GetReportsResponse401, GetReportsResponse404]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        date_from=date_from,
        date_to=date_to,
        currency=currency,
        report_types=report_types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: int,
    *,
    client: AuthenticatedClient,
    date_from: datetime.date,
    date_to: datetime.date,
    currency: Union[Unset, str] = UNSET,
    report_types: GetReportsReportTypes,
) -> Optional[Union[GetReportsResponse200, GetReportsResponse400, GetReportsResponse401, GetReportsResponse404]]:
    """Retrieve statistics for a single store

     Returns statistics for specified report types.

    You need to specify the report types you want to retrieve in the `report_types` query parameter as a
    comma-separated list,
    e.g. `report_types=sales_and_costs,profit`.

    **Note**: You cannot get statistics for a period longer than 6 months.

    #### Example

    To get statistics in the default currency of a store for `sales_and_costs` and `profit` reports for
    August 2022, you can use the
    following
    URL: https://api.printful.com/v2/stores/{id}/statistics?report_types=sales_and_costs,profit&date_fro
    m=2022-08-01&date_to=2022-08-31.

    ### Report types

    Currently, the following report types are available:

    | Report type                | Description                                              |
    |----------------------------|----------------------------------------------------------|
    | `sales_and_costs`          | Detailed information on sales and costs grouped by date. |
    | `sales_and_costs_summary`  | Short information on sales and costs grouped by date.    |
    | `printful_costs`           | Amount paid to Printful for fulfillment and shipping.    |
    | `profit`                   | Profit in the specified period.                          |
    | `total_paid_orders`        | The number of paid orders in the specified period.       |
    | `costs_by_amount`          | Information on costs by amount grouped by date.          |
    | `costs_by_product`         | Information on costs grouped by product.                 |
    | `costs_by_variant`         | Information on costs grouped by variant.                 |
    | `average_fulfillment_time` | Average time it took Printful to fulfill your orders.    |

    The response structure for the specific reports is documented in the response schema
    (`result.store_statistics.[reportName]`).

    Args:
        store_id (int):
        date_from (datetime.date):  Example: 2022-08-01.
        date_to (datetime.date):  Example: 2022-08-31.
        currency (Union[Unset, str]):  Example: USD.
        report_types (GetReportsReportTypes):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetReportsResponse200, GetReportsResponse400, GetReportsResponse401, GetReportsResponse404]
    """

    return sync_detailed(
        store_id=store_id,
        client=client,
        date_from=date_from,
        date_to=date_to,
        currency=currency,
        report_types=report_types,
    ).parsed


async def asyncio_detailed(
    store_id: int,
    *,
    client: AuthenticatedClient,
    date_from: datetime.date,
    date_to: datetime.date,
    currency: Union[Unset, str] = UNSET,
    report_types: GetReportsReportTypes,
) -> Response[Union[GetReportsResponse200, GetReportsResponse400, GetReportsResponse401, GetReportsResponse404]]:
    """Retrieve statistics for a single store

     Returns statistics for specified report types.

    You need to specify the report types you want to retrieve in the `report_types` query parameter as a
    comma-separated list,
    e.g. `report_types=sales_and_costs,profit`.

    **Note**: You cannot get statistics for a period longer than 6 months.

    #### Example

    To get statistics in the default currency of a store for `sales_and_costs` and `profit` reports for
    August 2022, you can use the
    following
    URL: https://api.printful.com/v2/stores/{id}/statistics?report_types=sales_and_costs,profit&date_fro
    m=2022-08-01&date_to=2022-08-31.

    ### Report types

    Currently, the following report types are available:

    | Report type                | Description                                              |
    |----------------------------|----------------------------------------------------------|
    | `sales_and_costs`          | Detailed information on sales and costs grouped by date. |
    | `sales_and_costs_summary`  | Short information on sales and costs grouped by date.    |
    | `printful_costs`           | Amount paid to Printful for fulfillment and shipping.    |
    | `profit`                   | Profit in the specified period.                          |
    | `total_paid_orders`        | The number of paid orders in the specified period.       |
    | `costs_by_amount`          | Information on costs by amount grouped by date.          |
    | `costs_by_product`         | Information on costs grouped by product.                 |
    | `costs_by_variant`         | Information on costs grouped by variant.                 |
    | `average_fulfillment_time` | Average time it took Printful to fulfill your orders.    |

    The response structure for the specific reports is documented in the response schema
    (`result.store_statistics.[reportName]`).

    Args:
        store_id (int):
        date_from (datetime.date):  Example: 2022-08-01.
        date_to (datetime.date):  Example: 2022-08-31.
        currency (Union[Unset, str]):  Example: USD.
        report_types (GetReportsReportTypes):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetReportsResponse200, GetReportsResponse400, GetReportsResponse401, GetReportsResponse404]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        date_from=date_from,
        date_to=date_to,
        currency=currency,
        report_types=report_types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: int,
    *,
    client: AuthenticatedClient,
    date_from: datetime.date,
    date_to: datetime.date,
    currency: Union[Unset, str] = UNSET,
    report_types: GetReportsReportTypes,
) -> Optional[Union[GetReportsResponse200, GetReportsResponse400, GetReportsResponse401, GetReportsResponse404]]:
    """Retrieve statistics for a single store

     Returns statistics for specified report types.

    You need to specify the report types you want to retrieve in the `report_types` query parameter as a
    comma-separated list,
    e.g. `report_types=sales_and_costs,profit`.

    **Note**: You cannot get statistics for a period longer than 6 months.

    #### Example

    To get statistics in the default currency of a store for `sales_and_costs` and `profit` reports for
    August 2022, you can use the
    following
    URL: https://api.printful.com/v2/stores/{id}/statistics?report_types=sales_and_costs,profit&date_fro
    m=2022-08-01&date_to=2022-08-31.

    ### Report types

    Currently, the following report types are available:

    | Report type                | Description                                              |
    |----------------------------|----------------------------------------------------------|
    | `sales_and_costs`          | Detailed information on sales and costs grouped by date. |
    | `sales_and_costs_summary`  | Short information on sales and costs grouped by date.    |
    | `printful_costs`           | Amount paid to Printful for fulfillment and shipping.    |
    | `profit`                   | Profit in the specified period.                          |
    | `total_paid_orders`        | The number of paid orders in the specified period.       |
    | `costs_by_amount`          | Information on costs by amount grouped by date.          |
    | `costs_by_product`         | Information on costs grouped by product.                 |
    | `costs_by_variant`         | Information on costs grouped by variant.                 |
    | `average_fulfillment_time` | Average time it took Printful to fulfill your orders.    |

    The response structure for the specific reports is documented in the response schema
    (`result.store_statistics.[reportName]`).

    Args:
        store_id (int):
        date_from (datetime.date):  Example: 2022-08-01.
        date_to (datetime.date):  Example: 2022-08-31.
        currency (Union[Unset, str]):  Example: USD.
        report_types (GetReportsReportTypes):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetReportsResponse200, GetReportsResponse400, GetReportsResponse401, GetReportsResponse404]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            client=client,
            date_from=date_from,
            date_to=date_to,
            currency=currency,
            report_types=report_types,
        )
    ).parsed
